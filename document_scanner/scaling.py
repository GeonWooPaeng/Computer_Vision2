# 크기 변환 
# 영상의 크기를 원본 영상보다 크게 or 작게 만드는 변환
# x축과 y축 방향으로의 스케일 비율(scale factor)를 지정

# '붙은 것은 확대 후
# x' = s1*x    -> s1 = w'/w  
# y' = s2*y    -> s2 = h'/h

import sys
import numpy as np
import cv2


src = cv2.imread('.\document_scanner.\\rose.bmp') # src.shape=(320, 480)

if src is None:
    print('Image load failed!')
    sys.exit()


# cv2.resize(src, dsize, dst, fx, fy, interpolation)
# dsize: 결과 영상 크기, (w, h) 튜플형태이며 (0,0)이면 fx와 fy값을 이용하여 결정 
# fx, fy: x와 y방향 스케일 비율(dsize값이 0일 때 유효)
# interpolation: 보간법 지정(중요), 영상의 퀄리티 결정

# 각 size에 4를 곱한 것들(size는 다 같다 => fx,fy 랑 dsize 둘중 하나만 써야된다.)
# 밑으로 갈수록 퀄리티가 좋아지지만 시간이 오래걸린다.
dst1 = cv2.resize(src, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST) # 퀄리티 가장 안 좋다.
dst2 = cv2.resize(src, (1920, 1280))  # cv2.INTER_LINEAR => 2 x 2 이용
dst3 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_CUBIC) # => 4 x 4
dst4 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_LANCZOS4) # => 8 x 8


cv2.imshow('src', src)

#[세로좌표, 가로좌표] 출력
cv2.imshow('dst1', dst1[500:900, 400:800]) 
cv2.imshow('dst2', dst2[500:900, 400:800])
cv2.imshow('dst3', dst3[500:900, 400:800])
cv2.imshow('dst4', dst4[500:900, 400:800])
cv2.waitKey()
cv2.destroyAllWindows()


# 영상의 축소 
# 디테일이 사라진다.
# 영상을 부드럽게 필터링한 후 축소, 다단계로 축소한다.
# 주로 cv2.INTER_AREA 플래그를 사용한다.

# 영상의 대칭
# cv2.flip(src, flipCode, dst)
# flipCode 에서 대칭을 지정한다 => 양수(+1) - 좌우 대칭, 0 - 상하 대칭, 음수(-1) - 좌우 & 상하 대칭
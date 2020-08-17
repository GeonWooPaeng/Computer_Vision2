# 허프 변환 직선 검출 
# 고차원 적인 에지를 검출하기 위한 것
# 2차원 영상 좌표에서의 직선 방정식을 parameter 공간으로 변환하여 직선을 찾는 알고리즘

# x,y를 a,b평면으로 해서 parameter을 찾는 방법(점 -> 직선)
# 축적 배열
# 직선 성분과 관련된 원소 값을 1씩 증가시키는 배열

# 직선의 방정식은 y축과 평행한 수직선을 표현 못함 -> xcos@ + ysin@ = p 극좌표계 직선의 방정식사용
# 점 -> 곡선 => 여기 곡선이 가장 많이 겹치는 점의 p,@ 값이 원래 p,@값이다.


import sys
import numpy as np
import cv2


src = cv2.imread('.\coin_count.\\building.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

edges = cv2.Canny(src, 50, 150)

#cv2.HoughLinesP() 에서 rho, theta를 작게 주면 축적 배열이 커진다.
# 축적 배열이 커진다 -> 정교해지지만 시간이 오래 걸린다.
#maxLineGap=5 - 5 pixel 떨어져도 line으로 인식
lines = cv2.HoughLinesP(edges, 1, np.pi / 180., 160,
                        minLineLength=50, maxLineGap=5) # => 선분의 시작과 끝 점을 찾아준다. 

# 직선 검출한 것을 화면에 보여주기 위한 것
dst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

if lines is not None:
    for i in range(lines.shape[0]):
        pt1 = (lines[i][0][0], lines[i][0][1])  # 시작점 좌표
        pt2 = (lines[i][0][2], lines[i][0][3])  # 끝점 좌표
        cv2.line(dst, pt1, pt2, (0, 0, 255), 2, cv2.LINE_AA)


cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()

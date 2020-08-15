# 영상의 기하학적 변환
# 영상을 구성하는 픽셀의 배치 구조를 변경하여 전체 영상의 모양을 바꾸는 작업

# 이동 변환
# 가로, 세로 방향으로 영상을 특정 크기만큼 이동시키는 것(x축, y축 변환)

import sys
import numpy as np
import cv2


src = cv2.imread('.\document_scanner.\\tekapo.bmp') #가로 640 세로 480

if src is None:
    print('Image load failed!')
    sys.exit()

aff = np.array([[1, 0, 200],
                [0, 1, 100]], dtype=np.float32) #가로 200, 세로 100 이동(float type으로 만들어줘야한다.)

dst = cv2.warpAffine(src, aff, (0, 0)) #이동변환하는 함수

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()

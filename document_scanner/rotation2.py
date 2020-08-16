import sys
import numpy as np
import cv2


src = cv2.imread('.\\document_scanner.\\tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

cp = (src.shape[1] / 2, src.shape[0] / 2)

# 특정 점을 중심으로 회전할 때 사용하는 함수
# cv2.getRotationMatrix2D(center, angle, scale)
# center: 회전 중심
# angle: 양수 - 반시계, 음수 - 시계
# scale: 확대 비율
# 출력: 2x3 어파인 변환 행렬, 실수형
rot = cv2.getRotationMatrix2D(cp, 20, 0.5)

dst = cv2.warpAffine(src, rot, (0, 0))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

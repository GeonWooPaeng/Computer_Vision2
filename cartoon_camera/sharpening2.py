#컬러 영상을 샤프닝 하기 

import sys
import numpy as np
import cv2

src = cv2.imread('.\cartoon_camera.\\rose.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

#float32를 한 이유: gaussianblur는 입력과 출력이 같으며 uint8로 하면 소수점이 다 잘립니다. 그러면 정교한 영상을 보여주지 못하기 때문에 float32를 사용한다 
src_f = src_ycrcb[:, :, 0].astype(np.float32) 
blr = cv2.GaussianBlur(src_f, (0, 0), 2.0)
src_ycrcb[:, :, 0] = np.clip(2. * src_f - blr, 0, 255).astype(np.uint8)

dst = cv2.cvtColor(src_ycrcb, cv2.COLOR_YCrCb2BGR)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

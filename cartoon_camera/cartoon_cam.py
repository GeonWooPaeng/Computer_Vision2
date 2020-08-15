# 카툰 필터 카메라
# 카메라 입력 영상에 실시간으로 필터링을 적용하는 기능 

# 기능 
# 카툰 필터 
# 스케치 필터 
# 스페이스바를 누를 때마다 모드 변경 

import sys
import numpy as np
import cv2


def cartoon_filter(img):
    #카툰 필터
    # 입력 영상의 색상을 단순화시키고, 에지 부분을 검정색으로 강조
    # 효과적으로 사용하기 위해 크기를 줄이고 보여줄때 확대해서 보여줘야 한다.

    # 크기 줄여주는 과정
    h, w = img.shape[:2]
    img2 = cv2.resize(img, (w//2, h//2))

    blr = cv2.bilateralFilter(img2, -1, 20, 7) # 영상 단순화
    edge = 255 - cv2.Canny(img2, 80, 120) # 에지 부분을 찾는 것(그레이스케일 영상으로 반환) , 255에서 빼는 이유는 에지부분을 검정색으로 하기 위함
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)

    #edge영상에서 흰색 부분은 blr을 그대로 가져오고 검정색(에지)부분은 blr을 0으로 채운다
    dst = cv2.bitwise_and(blr, edge) # 화면 합치기
    
    # 크기를 늘려주는 과정, interpolation=cv2.INTER_NEAREST은 값이 급격하게 바뀌는 느낌
    dst = cv2.resize(dst, (w, h), interpolation=cv2.INTER_NEAREST)

    return dst


def pencil_sketch(img):
    # 스케치 필터 
    # 평탄한 영역은 흰색
    # 에지중에서 어두운쪽 에지는 더 어둡게 밝은 에지는 흰색으로 표현 

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 그레이 스케일로 변환
    blr = cv2.GaussianBlur(gray, (0, 0), 3) #가우시안 블러
    dst = cv2.divide(gray, blr, scale=255) 

    
    return dst


cap = cv2.VideoCapture(0) # camera open

if not cap.isOpened():
    print('video open failed!')
    sys.exit()

cam_mode = 0 #mode에 따라 필터 부여

while True:
    ret, frame = cap.read()

    if not ret:
        break

    if cam_mode == 1:
        #카툰 필터
        frame = cartoon_filter(frame)

    elif cam_mode == 2:
        #스케치 필터
        frame = pencil_sketch(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)# 컬러로 변환

    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)

    if key == 27: #ESC 종료
        break
    elif key == ord(' '): #스페이스바 모드 변경
        cam_mode += 1
        if cam_mode == 3:
            cam_mode = 0


cap.release()
cv2.destroyAllWindows()

# 영상의 동전을 검출하여 금액이 얼마인지 자동으로 계산하는 프로그램 
# 동전 10원, 100원짜리만 있다고 가정 

# 구현할 기능 
# 1. 동전 검출하기 -> 허프 원 검출(cv2.HoughCircles() 사용)
# - 영상 크기: 800x600(px)
# - 동전 크기: 100원 - 약 100x100(px)
#              10원 - 약 80x80(px)

# 2. 동전 구분하기 -> 색상 정보 이용
# - 동전 영역 부분 영상 추출 -> HSV 색 공간으로 변환
# - 동전 영역에 대해서만 Hue 색 성분 분포 분석
# Hue 값(0~180)을 +40 시프트 하면 180이상이면 0이 된다.
# Hue 평균이 90 미만 -> 10원
# Hue 평균이 90 초과 -> 100원

import sys
import numpy as np
import cv2


# 입력 이미지 불러오기
src = cv2.imread('.\coin_count.\coins1.jpg')

if src is None:
    print('Image open failed!')
    sys.exit()

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
blr = cv2.GaussianBlur(gray, (0, 0), 1)

# 허프 변환 원 검출
circles = cv2.HoughCircles(blr, cv2.HOUGH_GRADIENT, 1, 50,
                           param1=150, param2=40, minRadius=20, maxRadius=80)

# 원 검출 결과 및 동전 금액 출력
sum_of_money = 0 #전체 금액을 저장할 공간
dst = src.copy()
if circles is not None: #원이 검출된 경우
    for i in range(circles.shape[1]): #각각의 원에 대한 정보 추출(circles.shape[1]->원의 개수)
        cx, cy, radius = circles[0][i]
        cv2.circle(dst, (cx, cy), radius, (0, 0, 255), 2, cv2.LINE_AA) #원을 빨간색으로 표현

        # 동전 영역 부분 영상 추출
        # radius는 실수 값
        x1 = int(cx - radius)
        y1 = int(cy - radius)
        x2 = int(cx + radius)
        y2 = int(cy + radius)
        radius = int(radius)
        
        crop = dst[y1:y2, x1:x2, :] #입력영상에서 동전 영역 부분영상을 짤라내는 곳
        ch, cw = crop.shape[:2]

        # 동전 영역에 대한 ROI 마스크 영상 생성
        mask = np.zeros((ch, cw), np.uint8) # 검정색 배경으로 한다.
        cv2.circle(mask, (cw//2, ch//2), radius, 255, -1) #radius를 이용해서 원을 흰색으로 채운다

        # 동전 영역 Hue 색 성분을 +40 시프트하고, Hue 평균을 계산
        hsv = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV) #crop된 영상을 HSV으로 변환
        hue, _, _ = cv2.split(hsv) #hue, situation, value라는 3개의 plain으로 나눠진다.
        hue_shift = (hue + 40) % 180 # +40 shift한다.
        mean_of_hue = cv2.mean(hue_shift, mask)[0] # mask를 줘서 원 안의 mean 값을 계산한다. # 100원짜리 인지 10원짜리인지 구별할 수 있는 지표

        # Hue 평균이 90보다 작으면 10원, 90보다 크면 100원으로 간주
        won = 100
        if mean_of_hue < 90:
            won = 10

        sum_of_money += won

        cv2.putText(crop, str(won), (20, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    0.75, (255, 0, 0), 2, cv2.LINE_AA)

cv2.putText(dst, str(sum_of_money) + ' won', (40, 80),
            cv2.FONT_HERSHEY_DUPLEX, 2, (255, 0, 0), 2, cv2.LINE_AA) #총액을 출력한다.

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()


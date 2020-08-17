#캐니 에지 검출
# 정확한 검출 
# 정학한 위치
# 단일 에지

#단계
#1. 가우시안 필터링 - 잡음 제거 목적(옵션)
#2. 그래디언트 계산(크기, 방향) - 주로 소벨 마스크를 사용 
#3. 비최대 억제 - 최대인 픽셀만 골라내서 그것을 에지 픽셀로 설정
#              - 그래디언트 방향에 위치한 두개의 픽셀을 조사하여 국지적 최대를 검사
#4. 히스테리시스 에지 트래킹 - 두개의 임계값을 사용(조명으로 인한 에지였다가 아니였다가 왔다갔다 하는 것을 막기 위함)
#                          - 검사할 때 중간 에지들이 강한 에지랑 만나면 에지라고 본다.(약한 에지쪽은 에지라고 하지 않는다.)

# => 회색으로 표현된 곳은 weak edge(약한 에지)부분
#- 회색이 흰색에 연결되어 있으면 에지라고 판단 O
#- 회색이 흰색에 연결되어 있지 않으면 에지라고 판단 X


import sys
import numpy as np
import cv2


src = cv2.imread('.\coin_count.\\building.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.Canny(src, 50, 150)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

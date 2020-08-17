# 문서 스캐너 
# 카메라로 촬영한 문서 영상을 똑바로 펴서 저장해주는 프로그램 

# 구현 기능
# 마우스로 문서 모서리 선택 & 이동하기
# 키보드 enter key 인식
# 왜곡된 문서 영상을 직사각형 형태로 똑바로 펴기(투시 변환)

import sys
import numpy as np
import cv2


def drawROI(img, corners):
    cpy = img.copy()

    c1 = (192, 192, 255) #1번 color
    c2 = (128, 128, 255) #2번 color

    # 4개의 원을 그리는 곳
    for pt in corners:
        cv2.circle(cpy, tuple(pt), 25, c1, -1, cv2.LINE_AA)

    # 4개의 원을 잇는 직선
    cv2.line(cpy, tuple(corners[0]), tuple(corners[1]), c2, 2, cv2.LINE_AA)
    cv2.line(cpy, tuple(corners[1]), tuple(corners[2]), c2, 2, cv2.LINE_AA)
    cv2.line(cpy, tuple(corners[2]), tuple(corners[3]), c2, 2, cv2.LINE_AA)
    cv2.line(cpy, tuple(corners[3]), tuple(corners[0]), c2, 2, cv2.LINE_AA)

    # 합성(조금 느릴 수 있다.) => 점 밑에 있는 그림이 보인다.
    disp = cv2.addWeighted(img, 0.3, cpy, 0.7, 0)

    return disp


def onMouse(event, x, y, flags, param):
    # 5개 parameter 다 있어야 한다.
    # event: 어떤 마우스 이벤트 
    # flags: 어떤 키가 눌러져 있냐
    # param: 어떤 데이터를 보내고 싶을 때 
    global srcQuad, dragSrc, ptOld, src

    # 마우스 눌렸을 때 
    if event == cv2.EVENT_LBUTTONDOWN:
        for i in range(4):
            # 핑크색 원 내부를 눌렀는지 확인하는 것
            if cv2.norm(srcQuad[i] - (x, y)) < 25:
                dragSrc[i] = True
                ptOld = (x, y) #드레그를 할때 원이 이동하는 변위 알기 위함
                break

    # 마우스를 땔때 
    if event == cv2.EVENT_LBUTTONUP:
        for i in range(4):
            dragSrc[i] = False

    # 마우스 움직이는 것
    if event == cv2.EVENT_MOUSEMOVE:
        for i in range(4):
            if dragSrc[i]: #마우스가 클릭되어 있는지 확인
                dx = x - ptOld[0] # 현재점 - 이전점
                dy = y - ptOld[1]

                srcQuad[i] += (dx, dy) #현재 모서리 좌표로 이동

                cpy = drawROI(src, srcQuad)
                cv2.imshow('img', cpy)
                ptOld = (x, y)
                break


# 입력 이미지 불러오기
src = cv2.imread('.\document_scanner.\scanned.jpg')

if src is None:
    print('Image open failed!')
    sys.exit()

# 입력 영상 크기 및 출력 영상 크기
h, w = src.shape[:2]
dw = 500 #똑바로 편 가로
dh = round(dw * 297 / 210)  # 똑바로 편 세로 (A4 용지 크기: 210x297cm)

# 모서리 점들의 좌표, 드래그 상태 여부
# 내가 선택하려고 하는 모서리점 4개 저장할 ndarray(초기점의 좌표) - 반시계방향(좌상, 좌하, 우하, 우상)
srcQuad = np.array([[30, 30], [30, h-30], [w-30, h-30], [w-30, 30]], np.float32)

# 반시계방향으로 출력영상의 4개의 모서리 위치
dstQuad = np.array([[0, 0], [0, dh-1], [dw-1, dh-1], [dw-1, 0]], np.float32)

#4개의 점 중 어떤 것을 드래그 했나 확인
dragSrc = [False, False, False, False]

# 모서리점, 사각형 그리기
disp = drawROI(src, srcQuad)

cv2.imshow('img', disp)
cv2.setMouseCallback('img', onMouse)

while True:
    key = cv2.waitKey()
    if key == 13:  # ENTER 키
        break
    elif key == 27:  # ESC 키
        cv2.destroyWindow('img')
        sys.exit()

# 투시 변환
pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
dst = cv2.warpPerspective(src, pers, (dw, dh), flags=cv2.INTER_CUBIC)

# 결과 영상 출력
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()

# 투시 변환
# 직사각형 형태의 영상이 자유도가 높은 임의의 사각형으로 만들어 내는 것
# 3 x 3 행렬로 표현이 된다. -> 미지수 8개 이다.
# cv2.getPerspectiveTransform(src, dst, solveMethod)
# 입력영상(src), 출력영상(dst) 4개의 좌표점을 
# numpy.ndarray.shape(4,2) => np.array([[x1,y1],[x2,y2],[x3,y3],[x4,y4]], np.float32) 같은 형태로 넣어주면 된다.


# cv2.warpAffine()
# affine 변환을 해서 출력 영상을 만들어 내는 함수
# 두번째 인자 -> 2 x 3 행렬(실수형)

# cv2.warpPerspective()
# perspective 변환을 해서 출력 영상을 만들어 내는 함수
# 두번째 인자 -> 3 x 3 행렬(실수형)

#찌그러진 명함 펴기
import sys
import numpy as np
import cv2


src = cv2.imread('.\document_scanner.\\namecard.jpg')

if src is None:
    print('Image load failed!')
    sys.exit()

w, h = 720, 400 #출력 영상 크기 정의

#입력영상 좌표(좌측상단, 우측상단, 오른쪽하단, 좌측하단)
srcQuad = np.array([[325, 307], [760, 369], [718, 611], [231, 515]], np.float32)

#출력영상 좌표(좌측상단, 우측상단, 오른쪽하단, 좌측하단)
dstQuad = np.array([[0, 0], [w-1, 0], [w-1, h-1], [0, h-1]], np.float32)

pers = cv2.getPerspectiveTransform(srcQuad, dstQuad) #3x3행렬을 리턴해준다.
dst = cv2.warpPerspective(src, pers, (w, h)) 

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()



# 어파인 변환
# 2 x 3 행렬로 표현 -> 미지수 6개 이다.
# 점 3개의 이동관계를 알면 점의 이동을 알려줄 수 있다.
# cv2.getAffineTransform(src, dst)
# 입력영상(src), 출력영상(dst) 3개의 좌표점을 
# numpy.ndarray.shape(3,2) => np.array([[x1,y1],[x2,y2],[x3,y3]], np.float32) 같은 형태로 넣어주면 된다.

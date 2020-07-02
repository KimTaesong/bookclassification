import sys
import cv2
import numpy as np


src = cv2.imread('opencv/images/namecard1.jpg')

if src is None:
    print('image load failed')
    sys.exit()

# src = cv2.resize(src, (640, 480))
src = cv2.resize(src, (0, 0), fx=0.5, fy=0.5)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 이렇게 쓰면 안됨, 2개의 값을 return 하기 때문에 범위를 지정
# src_bin = cv2.threshold(src_gray, 130, 255, cv2.THRESH_BINARY)

# _, src_bin = cv2.threshold(src_gray, 147, 255, cv2.THRESH_BINARY)

# OTSU 방법으로 자동으로 threshold값을 결정하는 알고리즘, 대표값 0으로 지정
th, src_bin = cv2.threshold(src_gray, 0, 255,
                            cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print(th)

contours, _ = cv2.findContours(src_bin, cv2.RETR_EXTERNAL,
                               cv2.CHAIN_APPROX_NONE)
print(len(contours))
# 88개의 객체 중에서 내가 원하는 명함 객체를 검출하는 방법

# pts 리스트, ndarray, kx1x2로 되어 있는 좌표라고 보면 됨
# 일단 전체 외곽선에 대한 그림을 그림, (0, 0, 255) 빨간색 라인
# for pts in contours:
#     cv2.polylines(src, pts, True, (0, 0, 255))
# 이진화된영상에서  위에 있는 자잘한 것들은 빼줘야 함 - 가장 간단한 방법
# 모든 외곽선을 검사하는데 면적이 1000보다 작다면
for pts in contours:
    if cv2.contourArea(pts) < 1000:
        continue

    approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True)*0.02, True)

    # 사각형 형태로 근사화 되지 않으면 무시
    if len(approx) != 4:
        continue

    w, h = 900, 500
    # 0번 3번째 왼쪽에 있는 2개의 점 , 1번, 2번은 오른쪽에 있는 2개 점인걸 알 수 있음
    # 3번째가 좌측 상단, 0번째 좌측 하단, -y좌표 작은게 상단
    # 1번째가 아래에 있는 점 2번째가 위에 있는 점
    srcQuad = np.array([[approx[0, 0, :]], [approx[1, 0, :]],
                        [approx[2, 0, :]], [approx[3, 0, :]]]).astype(np.float32)

    dstQuad = np.array([[0, 0], [w, 0], [w, h], [0, h]]).astype(np.float32)
    dstQuad = np.array([[0, h], [w, h], [w, 0], [0, 0]]).astype(np.float32)

    pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
    # 이미지를 잘라서 확대하니 뿌여짐
    dst = cv2.warpPerspective(src, pers, (w, h))

    cv2.polylines(src, pts, True, (0, 0, 255))

cv2.imshow('src', src)
cv2.imshow('src_gray', src_gray)
cv2.imshow('src_bin', src_bin)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()

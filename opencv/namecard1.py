import sys
import cv2


src = cv2.imread('opencv/images/books1.png')

if src is None:
    print('image load failed')
    sys.exit()

# src = cv2.resize(src, (640, 480))
src = cv2.resize(src, (0, 0), fx=1, fy=1)

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
    # if cv2.contourArea(pts) < 10:
    #     continue

    approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True)*0.02, True)

    # # 사각형 형태로 근사화 되지 않으면 무시
    # if len(approx) != 4:
    #     continue

    cv2.polylines(src, pts, True, (0, 0, 255))

cv2.imshow('src', src)
cv2.imshow('src_gray', src_gray)
cv2.imshow('src_bin', src_bin)

cv2.waitKey()
cv2.destroyAllWindows()

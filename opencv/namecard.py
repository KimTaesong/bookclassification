import sys
import cv2


src = cv2.imread('opencv/images/books1.png')

if src is None:
    print('image load failed')
    sys.exit()

# src = cv2.resize(src, (640, 480))
src = cv2.resize(src, (0, 0), fx=2, fy=2)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 이렇게 쓰면 안됨, 2개의 값을 return 하기 때문에 범위를 지정
# src_bin = cv2.threshold(src_gray, 130, 255, cv2.THRESH_BINARY)

# _, src_bin = cv2.threshold(src_gray, 147, 255, cv2.THRESH_BINARY)

# OTSU 방법으로 자동으로 threshold값을 결정하는 알고리즘, 대표값 0으로 지정
th, src_bin = cv2.threshold(src_gray, 0, 255,
                            cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print(th)
cv2.imshow('src', src)
cv2.imshow('src_gray', src_gray)
cv2.imshow('src_bin', src_bin)

cv2.waitKey()
cv2.destroyAllWindows()

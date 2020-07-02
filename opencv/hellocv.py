import cv2
import sys

# opencv에서 불러온 영상 데이터를 numpy.ndarray 형태로 불러온다.
img = cv2.imread('opencv/images/cat.bmp', cv2.IMREAD_GRAYSCALE)


# 파일을 못 불러올 때의 에러 처리를 해주는 게 중요
# 예외 처리 코드를 항상 작성하는 게 중요.
if img is None:
    print('Image load failed!')
    sys.exit()

print(type(img))
# B, G, R 순서로 컬러 정보가 저장
print(img.shape)
# 0~255부터 정수를 표현할 수 있는 데이터 타입을 사용 중.
print(img.dtype)
# 새로운 창을 만들어주는 함수 : image라는 이름의 문자열로 구분
cv2.namedWindow('image')
# 영상을 출력
cv2.imshow('image', img)
# key 입력을 기다리는 함수, 인자를 줄 수도 있음, 밀리 세컨드 단위의 키보드 입력을 기다림
# 아무런 숫자를 안 쓰거나 0을 넣으면 키보드 입력을 무한히 기다림.
while True:
    if cv2.waitKey() == 27:  # 아스키 코드 ESC
        break
# 만들어져있는 모든 창을 닫아라.
cv2.destroyAllWindows()


print('Hello OpenCv', cv2.__version__)

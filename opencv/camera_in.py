import sys
import cv2

# 비디오캡쳐 클래스를 이용해서 카메라 또는 비디오 파일을 처리할 수 있음
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('opencv/images/vtest.avi')
if not cap.isOpened():
    print('Camer open failed')
    sys.exit()

# 무한 루프 1프레임씩 가져옴
while True:
    ret, frame = cap.read()

    # 프레임이 문제가 있으면 종료
    if not ret:
        break
    # if frame is None:
    #     break

    # Canny edge검출알고리즘을 이용해서 frame 영상을 edge를 검출하기 위한 파라미터 50, 150
    # edge - 넘파이 배열, while루프안에서는 frame이라는 것은 동영상의 개념이 사라짐
    # 한 프레임 받아 왔으면 정지 영상이어서 정지 영상의 처리 알고리즘을 다 적용할 수 있음 밝기 조절, 색상 변환 다 할 수 있음
    edge = cv2.Canny(frame, 50, 150)
    # 한 프레임을 정상으로 받아왔다는 뜻
    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)
    if cv2.waitKey(20) == 27:
        break


cap.release()
cv2.destroyAllWindows()

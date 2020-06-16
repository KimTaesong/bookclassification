import cv2
import numpy as np


def showcam():
    try:
        cap = cv2.VideoCapture(0)
        print('open cam')
    except:
        print('Not working')
        return

    while True:
        ret, frame = cap.read()
        print(frame.shape)
        left_frame = frame[0:160, 0:240]
        right_frame = frame[0:160, 241:480]
        under_left_frame = frame[161:320, 0:240]
        under_right_frame = frame[161:320, 241:480]
        if not ret:
            print('error')
            break
        cv2.imshow('frame', frame)
        cv2.imshow('left_frame', left_frame)
        cv2.imshow('right_frame', right_frame)
        cv2.imshow('under_left_frame', under_left_frame)
        cv2.imshow('under_right_frame', under_right_frame)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


showcam()

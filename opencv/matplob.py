import matplotlib.pyplot as plt
import cv2


# 컬러 영상 출력
imgBGR = cv2.imread('opencv/images/cat.bmp')
# BGR채널을 RGB 채널로 바꿔준다.
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
plt.axis('off')
plt.imshow(imgRGB)
plt.show()

# 그레이 스케일 영상 출력
imgGray = cv2.imread('opencv/images/cat.bmp', cv2.IMREAD_GRAYSCALE)
plt.axis('off')
# cmap : colormap을 gray로 지정
plt.imshow(imgGray, cmap='gray')
plt.show()

# 두 개의 영상을 함께 출력
plt.subplot(121), plt.axis('off'), plt.imshow(imgRGB)
plt.subplot(122), plt.axis('off'), plt.imshow(imgGray, cmap='gray')
plt.show()

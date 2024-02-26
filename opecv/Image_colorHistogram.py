import cv2
from matplotlib import pyplot as plt

# 이미지 불러오기
image = cv2.imread('../data/11.png')  # 'your_image.jpg'를 원하는 이미지 경로로 바꿔주세요.

# BGR 색상 채널을 RGB로 변환
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 각 색상 채널에 대한 히스토그램 계산
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv2.calcHist([image_rgb], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])

plt.title('Color Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.show()
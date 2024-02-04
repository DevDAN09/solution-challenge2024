import cv2
import numpy as np

def white_balance_grayworld(img):
    # 이미지의 각 채널 평균을 계산
    avg_color_per_row = np.average(img, axis=0)
    avg_color = np.average(avg_color_per_row, axis=0)
    avg_rgb = np.mean(avg_color)

    # 각 채널에 대한 스케일 비율을 계산
    scale = avg_rgb / avg_color

    # 조정된 채널 값을 가진 새 이미지 생성
    balanced_img = np.zeros_like(img)
    for i in range(3):
        balanced_img[:, :, i] = img[:, :, i] * scale[i]

    # 값이 0-255 범위를 벗어나지 않도록 조정
    balanced_img = np.clip(balanced_img, 0, 255).astype(np.uint8)
    return balanced_img

# 이미지 불러오기 및 화이트 밸런스 조정
image = cv2.imread('../data/11.png')  # 이미지 경로 수정
white_balanced_image = white_balance_grayworld(image)

# 결과 이미지 표시
cv2.imshow('Original Image', image)
cv2.imshow('White Balanced Image', white_balanced_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

def increase_brightness(img, value=50):
    h, w = img.shape[:2]
    brightness = np.full((h, w, 3), value, dtype=np.uint8)
    brightened_img = cv2.add(img, brightness)
    return brightened_img

image_path = '../data/11.png'  # 이미지 경로 수정
image = cv2.imread(image_path)

if image is None:
    print(f"이미지를 불러오는데 실패했습니다: {image_path}")
else:
    brightened_image = increase_brightness(image, 50)
    cv2.imshow('Original Image', image)
    cv2.imshow('Brightened Image', brightened_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

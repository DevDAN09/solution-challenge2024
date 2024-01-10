import cv2
import numpy as np

def detect_color(img, lower_bound, upper_bound):
    # HSV 색 공간으로 변환
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 색상 범위에 해당하는 부분을 마스크로 생성
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # 마스크를 원본 이미지에 적용
    result = cv2.bitwise_and(img, img, mask=mask)

    # 마스크에 있는 흰색 픽셀의 수를 계산
    count = cv2.countNonZero(mask)
    return result, count

# 이미지 불러오기
image = cv2.imread('../data/11.png')  # 'your_image.jpg'를 원하는 이미지 경로로 바꿔주세요.

# 각 색상의 HSV 범위 정의
color_bounds = {
    "green": (np.array([50, 100, 100]), np.array([70, 255, 255])), # 담즙이 많이 섞일 경우, 엽록소 함유 음식 섭취, 큰 문제 없음
    "yellow": (np.array([25, 100, 100]), np.array([35, 255, 255])), # 모유수유시 많이 발생, 정상
    "brown": (np.array([10, 100, 20]), np.array([20, 255, 200])), # 정상적인 poo
    "red": (np.array([0, 100, 100]), np.array([10, 255, 255])),  # 조금 검출되더라도 알려야 함
    "black": (np.array([0, 0, 0]), np.array([180, 255, 30])) # 생 후 1주일까지는 정상, 이후 의사의 상담 요망, 일반적으로 모든변이 검정색임
}

# 각 색상 감지 및 결과 및 픽셀 수 표시
for color, (lower, upper) in color_bounds.items():
    detected, count = detect_color(image, lower, upper)
    print(f"{color} color detected pixels: {count}")
    cv2.imshow(f"{color} Color Detection", detected)

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

def enhance_contrast_histogram_equalization(image):
    # 이미지를 그레이스케일로 변환
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 히스토그램 평활화 적용
    equalized = cv2.equalizeHist(gray)

    return equalized

# 이미지 불러오기
image = cv2.imread('../data/11.png')  # 이미지 경로 수정

# 명암 대비 향상
enhanced_image = enhance_contrast_histogram_equalization(image)

# 결과 이미지 표시
cv2.imshow('Original Image', image)
cv2.imshow('Enhanced Contrast Image', enhanced_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

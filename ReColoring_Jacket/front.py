import cv2
import numpy as np

image = cv2.imread('front.jpg')

if image is None:
    print("이미지를 읽을 수 없습니다.")
else:
    height, width, _ = image.shape

pixel_colors = []


for y in range(height):
    temp_list = []
    for x in range(width):

        b, g, r = image[y, x]
        color_code = [b,g,r]

        #메인
        if (b>40 and g>40 and r>40) and (b<80 and g<80 and r<80):
            color_code = [176,231,255]
        #로고
        if (b>90 and r>180) and (b<130 and r<230) and not (r==g==b):    
             color_code = [176,231,255]
        #로고 테두리
        if (b>20 and r>70) and (b<120 and r<170) and not(r==g==b):
             color_code = [176,231,255]
        #팔쪽 로고
        if (b > 80 and g> 100 and r > 170) and (b<140 and g<170 and r<240) and not (r==g==b):
            color_code = [114,179,194]

        temp_list.append(color_code)
    pixel_colors.append(temp_list)

file = open("binary.txt","w")

for i in pixel_colors:
    file.writelines(str(i))

image_array = np.array(pixel_colors, dtype=np.uint8)    

cv2.imshow('Image', image_array)
cv2.waitKey(0)
cv2.destroyAllWindows()

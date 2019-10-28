#调试文件，无需采用

import cv2
res_content2={'location': {'height': 179, 'left': 84, 'top': 130, 'width': 203}}
cimg = cv2.imread('D:/appTh/0001.jpg')
conner1_x = int(res_content2["location"]["left"] )
conner1_y = int(res_content2["location"]["top"] )
conner2_x = int(res_content2["location"]["left"] +  res_content2["location"]["width"])
conner2_y = int(res_content2["location"]["top"] +  res_content2["location"]["height"])
cv2.rectangle(cimg, (conner1_x, conner1_y), (conner2_x, conner2_y), (224, 96, 108), 5)
cv2.imshow('labelOf', cimg)
cv2.waitKey(0)





import os

import cv2


# read image
image_path = os.path.join('.', 'data', 'bird.jpg')

img = cv2.imread(image_path)

# write image

cv2.imwrite(os.path.join('.', 'data', 'bird_out.jpg'), img)

# visualize image

cv2.imshow('pimi_frame', img)
cv2.waitKey(0) #opened untile press a key
# cv2.waitKey(5000) #opened for 5000 ms or 5 s

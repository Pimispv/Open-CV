import cv2
import os
image_path = os.path.join('.', 'data', 'bird.jpg')

image = cv2.imread(image_path)

print(image.shape)

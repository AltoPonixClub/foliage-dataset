import cv2
import numpy as np
import os
import random

# from scipy.ndimage.filters import gaussian_filter

# img = cv2.resize(cv2.imread("Checkerboard.png"), (480, 360))
# M = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=np.float32) * 0.5

# M = gaussian_filter(M, sigma=0.3)
# # print(M)
# # print(np.identity(3))
# img = cv2.warpPerspective(img, M, (480, 360))
# cv2.imshow("win", img)
# cv2.waitKey(0)

# For each image in directory, apply brightness and contrast augmentations 
# and save the result in the same directory

input_path = "/Users/aniketjain/Desktop/Code/AltoPonix/foliage-dataset/data_aug"
output_path = "/Users/aniketjain/Desktop/Code/AltoPonix/foliage-dataset/data_aug"

def brightness(filename, input_path, brightness_factor):
	if filename.endswith(".png"):
		# Apply brightness and contrast augmentations and save to output_path
		value = random.uniform(brightness_factor[0], brightness_factor[1])
		print(value)
		img = cv2.imread(input_path + "/" + filename)
		hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		hsv = np.array(hsv, dtype = np.float64)
		hsv[:,:,1] = hsv[:,:,1]*value
		hsv[:,:,1][hsv[:,:,1]>255]  = 25
		hsv[:,:,2] = hsv[:,:,2]*value 
		hsv[:,:,2][hsv[:,:,2]>255]  = 255
		hsv = np.array(hsv, dtype = np.uint8)
		img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
		cv2.imwrite(filename[:-4]+"a"+".png", img)

for filename in os.listdir(input_path):
	brightness(filename, input_path, [1.2, 2.5])
import cv2
import numpy as np
import os
import random
from PIL import Image, ImageEnhance
import timeit


input_path = "/Users/aniketjain/Desktop/Code/AltoPonix/foliage-dataset/data_aug"
output_path = "/Users/aniketjain/Desktop/Code/AltoPonix/foliage-dataset/data_aug"

def contrast(filename, input_path, contrast_factor, name):
	if filename.endswith(".png"):
		ImageEnhance.Contrast(Image.open(input_path + "/" + filename)).enhance(random.uniform(contrast_factor[0], contrast_factor[1])).save(filename[:-4]+ "_" + name + ".png")
		# Apply contrast augmentations and save to output_path
		# factor = random.uniform(contrast_factor[0], contrast_factor[1])
		# img = Image.open(input_path + "/" + filename)
		# enhancer = ImageEnhance.Contrast(img)
		# product = enhancer.enhance(factor)
		# product.save(filename[:-4]+ "_" + name + ".png")

def brightness(filename, input_path, brightness_factor, name):
	if filename.endswith(".png"):
		ImageEnhance.Brightness(Image.open(input_path + "/" + filename)).enhance(random.uniform(brightness_factor[0], brightness_factor[1])).save(filename[:-4]+ "_" + name + ".png")		# Apply brightness augmentations and save to output_path
		# value = random.uniform(brightness_factor[0], brightness_factor[1])
		# print(filename, value)
		# img = Image.open(input_path + "/" + filename)
		# enhancer = ImageEnhance.Brightness(img)
		# product = enhancer.enhance(value)
		# product.save(filename[:-4]+ "_" + name + ".png")


for filename in os.listdir(input_path):
	# Increase brightness in range I tested to be acceptable
	brightness(filename, input_path, [1.2, 2.5], "a") 
	# Decrease contrast in range I tested to be acceptable
	contrast(filename, input_path, [0.2, 0.8], "b")


# from scipy.ndimage.filters import gaussian_filter

# img = cv2.resize(cv2.imread("Checkerboard.png"), (480, 360))
# M = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=np.float32) * 0.5

# M = gaussian_filter(M, sigma=0.3)
# # print(M)
# # print(np.identity(3))
# img = cv2.warpPerspective(img, M, (480, 360))
# cv2.imshow("win", img)
# cv2.waitKey(0)

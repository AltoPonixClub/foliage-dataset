import os
import random
from PIL import Image, ImageEnhance, ImageOps

from wand.image import Image
import numpy as np
import cv2


input_path = "./data_aug"
output_path = "./data_aug"

def contrast(filename, input_path, contrast_factor, name):
	ImageEnhance.Contrast(Image.open(input_path + "/" + filename)).enhance(random.uniform(contrast_factor[0], contrast_factor[1])).save(filename[:-4]+ "_" + name + ".png")
	# Apply contrast augmentations and save to output_path
	# factor = random.uniform(contrast_factor[0], contrast_factor[1])
	# img = Image.open(input_path + "/" + filename)
	# enhancer = ImageEnhance.Contrast(img)
	# product = enhancer.enhance(factor)
	# product.save(filename[:-4]+ "_" + name + ".png")

def brightness(filename, input_path, brightness_factor, name):
	ImageEnhance.Brightness(Image.open(input_path + "/" + filename)).enhance(random.uniform(brightness_factor[0], brightness_factor[1])).save(filename[:-4]+ "_" + name + ".png")		# Apply brightness augmentations and save to output_path
	# value = random.uniform(brightness_factor[0], brightness_factor[1])
	# print(filename, value)
	# img = Image.open(input_path + "/" + filename)
	# enhancer = ImageEnhance.Brightness(img)
	# product = enhancer.enhance(value)
	# product.save(filename[:-4]+ "_" + name + ".png")

def posterize(filename, input_path, bits, name): # Reduce color in an image. Basically deep fries it
	ImageOps.posterize(Image.open(input_path + "/" + filename).convert('RGB'), bits).save(filename[:-4]+ "_" + name + ".png")
	# posterize / deep fry the image
	# img = Image.open(input_path + "/" + filename)
	# img = img.convert('RGB') # bc posterize only works on RGB images and PNG doesn't count
	# img = ImageOps.posterize(img, bits)
	# img.save(filename[:-4]+ "_" + name + ".png")

def barrel(filename, input_path, name):
	with Image(filename=(input_path + "/" + filename)) as img: # sry for double use of `filename`
		img.virtual_pixel = 'transparent'
		img.distort('barrel', (0.2, 0.0, 0.0, 1.0))
		img.save(filename=filename[:-4]+ "_" + name + ".png")
		# convert to opencv/numpy array format

for filename in os.listdir(input_path):
	if filename.endswith(".png"):
		# # Increase brightness in range I tested to be acceptable
		# brightness(filename, input_path, [1.2, 2.5], "a") 
		# # Decrease contrast in range I tested to be acceptable
		# contrast(filename, input_path, [0.2, 0.8], "b")
		# # Decrease color in image to certain number of bits per channel. Higher number = less deep fried
		# posterize(filename, input_path, 8, "c")
		# Barrel distortion, range, in `barrel_factor` param, coming soon
		barrel(filename, input_path, "d")





# import PIL.ImageOps
# import cv2
# import numpy as np
# from scipy.ndimage.filters import gaussian_filter

# img = cv2.resize(cv2.imread("Checkerboard.png"), (480, 360))
# M = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=np.float32) * 0.5

# M = gaussian_filter(M, sigma=0.3)
# # print(M)
# # print(np.identity(3))
# img = cv2.warpPerspective(img, M, (480, 360))
# cv2.imshow("win", img)
# cv2.waitKey(0)

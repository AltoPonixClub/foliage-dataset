import cv2
import numpy as np
from scipy.ndimage.filters import gaussian_filter

img = cv2.resize(cv2.imread("Checkerboard.png"), (480, 360))
M = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=np.float32) * 0.5

M = gaussian_filter(M, sigma=0.3)
# print(M)
# print(np.identity(3))
img = cv2.warpPerspective(img, M, (480, 360))
cv2.imshow("win", img)
cv2.waitKey(0)

# USAGE
# python index.py

# import the necessary packages
import numpy as np
import argparse
import imutils
import cv2

# construct the argument parser and parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", type=str, default="opencv_logo.png",
	help="path to the input image")
args = parser.parse_args()

# load the image and display it to our screen
image = cv2.imread(args.image)
cv2.imshow("Original", image)

height = image.shape[0]
width = image.shape[1]
# # shift the image 25 pixels to the right and 50 pixels down
M = np.float32([[1, 0, 25], [0, 1, 50]])
print(M)
shifted = cv2.warpAffine(image, M, (width, height))
cv2.imshow("Shifted Down and Right", shifted)

# # now, let's shift the image 50 pixels to the left and 90 pixels
# # up by specifying negative values for the x and y directions,
# # respectively
M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (width, height))
cv2.imshow("Shifted Up and Left", shifted)

# use the imutils helper function to translate the image 100 pixels
# down in a single function call
shifted = imutils.translate(image, -90, 0)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)
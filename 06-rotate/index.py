# USAGE
# python rotate_simple.py --image images/saratoga.jpg

# import the necessary packages
import numpy as np
import argparse
import imutils
import cv2

# construct the argument parse and parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", type=str, default="saratoga.jpg",
	help="path to the image file")
args = parser.parse_args()

# load the image from disk
image = cv2.imread(args.image)

(w,h) = image.shape[:2]

rotated = imutils.rotate(image, -90)

cv2.imshow("rotated", rotated)
rotated_bound = imutils.rotate_bound(image, -90)
cv2.imshow("rotated_bound",rotated_bound)
cv2.waitKey(0)
# loop over the rotation angles
# for angle in np.arange(0, 360, 15):
# 	rotated = imutils.rotate(image, angle)
# 	cv2.imshow("Rotated (Problematic)", rotated)

# loop over the rotation angles again, this time ensuring
# no part of the image is cut off
# for angle in np.arange(0?
# USAGE
# python morphological_hats.py --image car.png

# import the necessary packages
import argparse
import cv2
import imutils

# construct the argument parser and parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", required=True,
	help="path to input image")
args = parser.parse_args()

# load the image and convert it to grayscale
image = cv2.imread(args.image)
cv2.imshow("Original", image)

# my own example for pringles barcode
# need to rotate the image
if ("pringles" in args.image ):
	image = imutils.rotate(image, -90)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# construct a rectangular kernel (13x5) and apply a blackhat
# operation which enables us to find dark regions on a light
# background
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))
blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel)

# similarly, a tophat (also called a "whitehat") operation will
# enable us to find light regions on a dark background
tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rectKernel)

# show the output images
cv2.imshow("Blackhat", blackhat)
cv2.imshow("Tophat", tophat)
cv2.waitKey(0)
# USAGE
# python simple_thresholding.py --image images/coins01.png

# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", type=str, required=True,
	help="path to input image")
args = parser.parse_args()

# load the image and display it
image = cv2.imread(args.image)
cv2.imshow("Image", image)

# convert the image to grayscale and blur it slightly
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)
cv2.imshow("Gray", gray)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)


# apply basic thresholding -- the first parameter is the image
# we want to threshold, the second value is our threshold
# check; if a pixel value is greater than our threshold (in this
# case, 200), we set it to be *black, otherwise it is *white*
(_, threshInv) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", threshInv)

# using normal thresholding (rather than inverse thresholding)
(_, thresh) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)

# using a morphological operation (closing worked the best)
# needed for coins01 example, but not needed for coins02 example
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
closing = cv2.morphologyEx(threshInv, cv2.MORPH_CLOSE, kernel)
cv2.imshow("closed", closing)
# dilation also works, but it also increases the sizes of our coins, something we don't want.


# visualize only the masked regions in the image
masked = cv2.bitwise_and(image, image, mask=threshInv)
cv2.imshow("Normal Output", masked)

masked = cv2.bitwise_and(image, image, mask=closing)
cv2.imshow("Output with closing operation", masked)
cv2.waitKey(0)
# USAGE
# python image_drawing.py

# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="adrian.png",
	help="path to the input image")
args = vars(ap.parse_args())

# load the input image from disk
image = cv2.imread(args["image"])

# draw a circle around my face, two filled in circles covering my
# eyes, and a rectangle over top of my mouth
red = (0, 0, 255)
cv2.circle(image, (168, 188), 90, red, 2)
cv2.line(image, (140,164),(160,164), red, 8)
cv2.line(image, (185,169),(205,174), red, 8)
# cv2.circle(image, (150, 164), 10, red, -1)
# cv2.circle(image, (192, 174), 10, red, -1)
cv2.line(image, (134,212),(186,215), red, 15)
# cv2.rectangle(image, (134, 200), (186, 218), red, -1)

# show the output image
cv2.imshow("Output", image)
cv2.waitKey(0)
# USAGE
# python index.py --image apple_support.png
# python index.py --image apple_support.png --digits 0

# import the necessary packages
import pytesseract
import argparse
import cv2

# construct the argument parser and parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")
parser.add_argument("-d", "--digits", type=int, default=1,
	help="whether or not *digits only* OCR will be performed")
args = parser.parse_args()

# load the input image, convert it from BGR to RGB channel ordering,
# and initialize our Tesseract OCR options as an empty string
image = cv2.imread(args.image)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
options = ""

# check to see if *digit only* OCR should be performed, and if so,
# update our Tesseract OCR options
if args.digits > 0:
	options = "outputbase digits"

# OCR the input image using Tesseract
text = pytesseract.image_to_string(rgb, config=options)
print(text)
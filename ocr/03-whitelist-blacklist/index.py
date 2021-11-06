# USAGE
# python index.py --image pa_license_plate.png
# python index.py --image pa_license_plate.png --blacklist "*#"
# python index.py --image invoice.png --whitelist "0123456789$.-"
# python index.py --image invoice.png --whitelist "0123456789.-" --blacklist "0"

# import the necessary packages
import pytesseract
import argparse
import cv2

# construct the argument parser and parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")
parser.add_argument("-w", "--whitelist", type=str, default="",
	help="list of characters to whitelist")
parser.add_argument("-b", "--blacklist", type=str, default="",
	help="list of characters to blacklist")
args = parser.parse_args()

# load the input image, swap channel ordering, and initialize our
# Tesseract OCR options as an empty string
image = cv2.imread(args.image)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
options = ""

# check to see if a set of whitelist characters has been provided,
# and if so, update our options string
if len(args.whitelist) > 0:
	options += "-c tessedit_char_whitelist={} ".format(
		args.whitelist)

# check to see if a set of blacklist characters has been provided,
# and if so, update our options string
if len(args.blacklist) > 0:
	options += "-c tessedit_char_blacklist={}".format(
		args.blacklist)

# OCR the input image using Tesseract
text = pytesseract.image_to_string(rgb, config=options)
print(text)
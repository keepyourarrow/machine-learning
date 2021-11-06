# USAGE
# python index.py --image pyimagesearch_address.png
# python index.py --image steve_jobs.png

# import the necessary packages
import pytesseract
import argparse
import cv2

# construct the argument parser and parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")
args = parser.parse_args()

# load the input image and convert it from BGR to RGB channel
# ordering
image = cv2.imread(args.image)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# use Tesseract to OCR the image
text = pytesseract.image_to_string(image)
print(text)
cv2.imshow("Image", image)
cv2.waitKey(0)
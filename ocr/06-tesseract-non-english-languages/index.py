# USAGE
# python index.py --image images/german.png --lang deu

# import the necessary packages
from textblob import TextBlob
import pytesseract
import argparse
import cv2

# construct the argument parser and parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")
parser.add_argument("-l", "--lang", required=True,
	help="language that Tesseract will use when OCR'ing")
parser.add_argument("-t", "--to", type=str, default="en",
	help="language that we'll be translating to")
parser.add_argument("-p", "--psm", type=int, default=13,
	help="Tesseract PSM mode")
args = parser.parse_args()

# load the input image and convert it from BGR to RGB channel
# ordering
image = cv2.imread(args.image)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# OCR the image, supplying the country code as the language parameter
options = "-l {} --psm {}".format(args.lang, args.psm)
text = pytesseract.image_to_string(rgb, config=options)
text = text.replace("\n", " ")

# show the original OCR'd text
print("ORIGINAL")
print("========")
print(text)
print("")

# translate the text to a different language
tb = TextBlob(text)
translated = tb.translate(to=args.to)

# show the translated text
print("TRANSLATED")
print("==========")
print(translated)
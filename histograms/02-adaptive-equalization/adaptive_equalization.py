# USAGE
# python adaptive_equalization.py --image images/boston.png

# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", type=str, required=True,
	help="path to the input image")
parser.add_argument("-c", "--clip", type=float, default=2.0,
	help="threshold for contrast limiting")
parser.add_argument("-t", "--tile", type=int, default=8,
	help="tile grid size -- divides image into tile x tile cells")
args = parser.parse_args()

# load the input image from disk and convert it to grayscale
print("[INFO] loading input image...")
image = cv2.imread(args.image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

(B,G,R) = cv2.split(image)

# apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
print("[INFO] applying CLAHE...")
clahe = cv2.createCLAHE(clipLimit=2.0,
	tileGridSize=(args.tile, args.tile))
eq = clahe.apply(B)
eq2 = clahe.apply(G)
eq3 = clahe.apply(R)

merged = cv2.merge([eq,eq2,eq3])

# show the original grayscale image and CLAHE output image
cv2.imshow("Input", image)
cv2.imshow("CLAHE", merged)
cv2.waitKey(0)
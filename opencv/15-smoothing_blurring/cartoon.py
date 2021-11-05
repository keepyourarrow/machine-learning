import cv2
import numpy as np
import argparse
import imutils

# construct the argument parser and parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", type=str, default="./images/cat.jpg",
	help="path to input image")
args = parser.parse_args()

# load the image, display it to our screen, and construct a list of
# bilateral filtering parameters that we are going to explore
image = cv2.imread(args.image)

image = imutils.resize(image, width=750)
cv2.imshow("Original", image)

def edge_mask(image, line_size, kernel):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.medianBlur(gray, kernel)
    print(gray)
    print(gray_blur)
    edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, line_size, kernel)
    return edges

def color_quantization(img, k):
    # Transform the image
    data = np.float32(img).reshape((-1, 3))

    # Determine criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)

    # Implementing K-Means
    ret, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    result = center[label.flatten()]
    result = result.reshape(img.shape)
    return result


line_size = 7
kernel = 7
edges = edge_mask(image, line_size, kernel)
cv2.imshow("Edges",edges)
cv2.waitKey(0)

total_color = 9
image = color_quantization(image, total_color)
cv2.imshow("Color_Quantization",image)
cv2.waitKey(0)

blurred = cv2.bilateralFilter(image, d=7, sigmaColor=200,sigmaSpace=200)
cv2.imshow("BilateralFilter", blurred)
cv2.waitKey(0)

cartoon = cv2.bitwise_and(blurred, blurred, mask=edges)
cv2.imshow("Cartoon", cartoon)
cv2.waitKey(0)
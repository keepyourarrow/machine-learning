## contours
1. How to compute center of a contour (shape)

## Goals
1. Detect the outline of each object
1. Compute the center of the contour

## How
1. We first *greyscale* the image
1. Then we Gaussian *blur* it to reduce the noise
1. Then we apply some kind of binarization, either a thresholding or a Canny edge detector
1. Thresholding in our case
1. *If we want to find multiple centers in images* we'd want to do it with contours
1. If it's only for one object then
M = cv2.moments(threshImage)
#### calculate x,y coordinate of center
cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])
#### put text and highlight the center
cv2.circle(img, (cX, cY), 5, (255, 255, 255), -1)
cv2.putText(img, "centroid", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
#### In our example shape_and_colors.png we have shapes of various sizes

## What is image moment
1. Average of intensities of an image pixels
1. Image moment is a weighted average of image pixel intensities, with help of which we can find specific properties of an image: centroid, area, radius, etc.
1. It's being calculated by ignoring *zero values*
1. M00 = area
1. Formula for centroid
1. The formula for x *x = M10 / M00*
1. For y *y = M01 / M00*

## how to find contours
#### cv2.RETR_EXTERNAL, cv2.RETR_LIST, cv2.RETR_TREE (are possible values, didn't seem to do anything in this example)
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
## how to draw contours

cv2.drawContours(image, cnts, -1, (0, 255, 0), 2)

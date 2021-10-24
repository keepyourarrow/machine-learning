# sorting
1. There is no built-in way to sort contours in opencv, but we can always make our own solution

## rundown
1. pretty much the same process until this point
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
1. then sort
(cnts, boundingBoxes) = sort_contours(cnts, method)
1. then draw numbers on the center of image moment
for (i, c) in enumerate(cnts):
	draw_contour(image, c, i)
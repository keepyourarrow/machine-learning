

## automatic edge detection algorithm

#### keep sigma as 0.33 (Adrian said that)

def auto_canny(image, sigma=0.33):
    #### get the median. Possible values: 143, 214, 75
	v = np.median(image)

	#### apply automatic Canny edge detection using the computed median
    #### Possible values for lower are: 95,143,50
	lower = int(max(0, (1.0 - sigma) * v))

    #### Possible values for upper 190,255,99
	upper = int(min(255, (1.0 + sigma) * v))

	edged = cv2.Canny(image, lower, upper)

	#### return the edged image
	return edged
# gamma
1. You can use gamma correction when you have a bad camera that you can't change and you know that gamma correction will help you out

## how

1. We convert our pixel intensities from range [0,255] to [0,1.0]
1. Apply the formula
#### image ^ (1 / value of gamma)
O = I ^ (1 / G)
1. We then scale [0,1.0] back to [0,255]
1. Gamma(G) value less than 1. G < 1 makes our image darker, G > 1 makes our image lighter

def adjust_gamma(image, gamma=1.0):
	#### that's the formula (O = I ^ (1 / G))
	invGamma = 1.0 / gamma
    #### builds a 256 length table where every value 1-256 (nothing to do with image pixels, this table is the same for every single image)
    #### our lookup table then compares values, so every value with pixel value 5 is gonna be replaced by 15, 7 is replaced with 20 and that's for every single pixel
    #### even if its 16000 pixels, it will very quickly go over every single pixel and replace its value accordingly
    #### The look up table does it very quickly
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
    #### transform to unsigned 8 bit integer

	#### apply gamma correction using the lookup table
	return cv2.LUT(image, table)

## how to show 2 images left-right
#### to put text
cv2.putText(adjusted, "g={}".format(gamma), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)

#### np.hstack
cv2.imshow("Images", np.hstack([original, adjusted]))
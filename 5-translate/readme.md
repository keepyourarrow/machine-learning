# opencv

## translating (method 1)

M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (width, height))
#### you create a multidimensional array where -50 and -90 are the values you are translating
#### -50 to the left (positive 50 if you want to move to the right) and -90 up (positive 90 to go down)
#### everything else should stay the same in the structure
#### then we call warpAffine method where we pass our params, simple enough...


## translating (method 2)
shifted = imutils.translate(image, -90, 0)
#### there is another way to translate, a much simpler way is to use imutils package that has a translate method

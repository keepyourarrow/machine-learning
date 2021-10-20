# adaptive thresholding
1. best used when shadows are involved
1. different illumination/lightning


## Why other thresholding methods won't work
1. Because only one value of *T* is being used, while we need several, due to shadows and illuminations interfering with the image

## How it works
1. Adaptive segmentation as the name suggests, only calculates small area of pixels at a time,applying a different *T* value to each area.
1. While basic thresholding calculates them with only one *T* value
1. We use either average mean or the Gaussian blur (refer to smoothing_blurring section)
1. So its pretty similar we have our square/rectangle kernel that goes over the whole image, one small section/area at the same time and calculates each pixel in that area by calculating it
1. T = mean(IL ) – C
1. and the C is the constant that we fine tune the threshold value of T
1. Gaussian thresholding is better

#### 1st argument is the image
#### 2nd argument is the color(we used the same one in other thresholhds)
#### 3rd argument is the type of blurring. There is also a cv2.ADAPTIVE_THRESH_GAUSSIAN_C
#### 4th argument same as always, probably the one we'd want to use cv2.THRESH_BINARY_INV
#### 5th argument is 21x21 (the number we want to fine tune, just pick and plug different numbers)
#### 6th argumetn is the constant C that we also want to fine tune
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 10)
#### or
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 4)



## When to use
1. If you are confident in the lightning, confident that there are no shadows on the image, then the answer is - Never
1. However, that's not always the case.

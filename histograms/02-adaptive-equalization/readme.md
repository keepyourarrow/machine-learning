# equalization
1. Adjusts global contrast by updating pixel intensity
1. It helps areas of low contrast to obtain a high contrast
1. There is a basic equalization and an adaptive one
1. Used by doctors to remove high contrast from x-ray or CT scans to help them give out a better diagnosis
1. Basic one is easy to use, but it can boost up noise

## How it works
1. It makes a histogram of an entire image
1. Takes the most frequent pixels and spreads them out

## Rundown
1. Apply to single channels (grayscale)
1. You can also split RGB channel into single channels and then merge them together, but that doesn't always work as it's supposed to.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

## adaptive equalizaiton
1. Same concept as adaptive thresholding, where rather than taking the whole image, we apply it to sets of grids and calculate separately

#### tileGridSize anywhere between 4 to 10 is fine
#### clipLimit = the lower the better in the (2-5 range)
clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
equalized = clahe.apply(grayImage)
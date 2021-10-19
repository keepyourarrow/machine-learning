# morhological-operations
### morphological operations are very important, they provide an elegant solution to some of the problems to which some of the computer vision practitioners would try to apply some of the more advanced computer vision, machine learning and deep learning techniques. "It seems that once you learn how to wield a hammer, each problem looks like a nail"
### while one of the morphological operation might've come in handy.
### For example you can detect a barcode in image without using any fancy techniques.
### "There will be a time when you'll be ready to swing a hammer down on a problem, only to realize that a more elegant, simple solution may already exist"

#### mostly applied to grayscale or binary images
#### used to OCR algorithms, detect barcodes, detect license plates etc (very needed for me)

## list of morphological operations
1. Erosion
1. Dilation
1. Opening
1. Closing
1. Morphological gradient
1. Black Hat
1. Top Hat

#### hats are in morhological_hats.py file


### rundown
1. first you load the image
2. then you convert it to grayscale (not needed if you already use a binary image)
3. thresholding/adaptive thresholding/edge detection (not needed if you are already using a binary image)

#### convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

## structuring element
#### a shape/a template that helps us perform morphological operations. It goes over the image

## erosion (-) symbol
#### in simple words, eroding means to make foreground of an image smaller
####  2nd argument is a kernel, if you don't provide anything a default 3x3 would be used
eroded = cv2.erode(gray.copy(), None, iterations=i + 1)
#### the more erosion iterations we apply to the image, the more destroyed foreground we would get, until we'd have no foreground left

## Why we need erosion
#### Well imagine we need to count the number of coins there are on the table, and some of those coins are touching each other, we humans understand that, but computer doesn't. By using erosion, just like how we collapse some of the letters, disconnecting strokes of the letters, we can also collapse the coins, disconnect them from each other.
#### also useful for removing blobs in an image (the noise) pyimagesearch_logo_noise.png

## dilation (+) symbol
#### opposite of erosion. We usually want to apply it after erosion, typically when we need the correct width, since erosion eats away at the width, dilation would help to get it back.
for i in range(0, 3):
	dilated = cv2.dilate(gray.copy(), None, iterations=i + 1)
	cv2.imshow("Dilated {} times".format(i + 1), dilated)
	cv2.waitKey(0)

## opening
#### erosion followed by dilation
#### best used when you want to remove the noise(blobs) from the image
#### first the erosion is applied to remove the blobs, then dilation is applied to regrow the size of the original object
#### first we get our kernel. 1st argument is the standard one, you can use others, but MORPH_RECT is the best one for our situation.
#### 2nd argument is the kernel size (7,7)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
#### 1st argument is image, 2nd is MORPH_OPEN, since we are using opening, 3rd argument is the kernel
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2.imshow("Opening", opening)
#### it completely removed the blobs(the noise), but it also eroded some of our letters, to heal them we'd want to use dilation after

## getStructuringElement types
1. cv2.MORPH_RECT = for rectangle
1. cv2.MORPH_CROSS = gets a cross shape structuring element
1. cv2.MORPH_ELLIPSE = circular structuring element
#### any can be used based on your image.

## closing
#### dilation followed by erosion (complete opposite of opening)
#### same as in opening
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
#### the only difference is that we are calling MORPH_CLOSE method not MORPH_OPEN
opening = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
cv2.imshow("CLOSING", opening)

## Morphological gradient
#### useful for determining the outline of a particular object(word) of an image
#### same as other examples, the only difference being the second argument (cv2.MORPH_GRADIENT)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

## white hat(top hat)
#### reveals bright regions on dark background
#### best suited for grayscale images (not binary ones)

## black hat
#### reveals dark regions on white background
#### best suited for grayscale images (not binary ones)

## hats
#### usually when you are making a structured element for grayscaled images, you need to correctly choose the kernel/template/matrix box that you want to use
#### since structured element is what's gonna be going over our image, we want the rectangle to fit
#### for the case of licence plate, it's much wider than it is taller, we want our rectangle to correlate with that by being a pretty wide rectangle
#### Example:
[[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]],
[[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]],
[[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]],
[[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]],
[[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]

rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))

#### black hat
blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel)

#### top hat
blackhat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rectKernel)

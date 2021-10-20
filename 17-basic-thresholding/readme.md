# thresholding
1. It's the binarization of an image. Taking a greyscale image and converting it to black and white.
1. One of the most common and basic segmentation techniques(we are gonna use it a lot, along with edge detection)
1. The process of separating our foreground(objects we are interested in) from the background
1. Helps us simplify the image
1. As a result it creates some noise that we need to perform morphological operations on

## rundown
1. we first need to greyscale the image, to remove all the colors, to decrease computing time
1. We then want to blur it using Gaussian blur with a (7,7) kernel. As we don't care about the details of the coin, we just want to accurately determine the shape of the coin, the edges.
1. Apply thresholding
1. Apply morphological operation (closing,opening)
    1. P.S While closing works on an image coins01.png and coins02.png, it doesn't work for opencv_logo.png as it merges the letters together
1. Use it as a mask with the original image

## Which thresholding do we use mostly
1. between normal and binary inverse thresholding, we'd normally use binary inverse, because its more standard to have black background and white foreground, especially when it comes to contours

## Why we have noise after thresholding
1. That means we failed the thresholding test. The value we supplied (200) was lower than the value of pixel on some of the coins
1. That comes from having a poor lightning. coins01 failed, but coins02 the image was well lit, so the test passed.
1. We can combat it by using a different thresholding strategy (otsu)

## normal thresholding
#### 1st parameter is an image
#### 2nd parameter - threshold value, a pixel value that is needed to perform a check
#### It's simple, all pixels that are greater than our threshold 200 will be set to white (255)
#### all pixels that are less than our threshold will be set to black
#### 3rd paremeter is what we want to make our background. For most cases, just keep it as white
p > 200 = 255 (3rd parameter)
p < 200 = 0
(_, thresh) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)

## binary inverse thresholding
#### same arguments as a normal thresholding
#### all pixels that are greater than 200 will be set to black
#### all pixels that are less than 200 will be set to white
p > 200 = 0
p < 200 = 255 (3rd parameter)
(_, threshInv) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY_INV)


## Why is it a pain to use a normal thresholding
1. Because we need to supply the threshold manually, and one threshold might not work for every image
1. To kinda combat that we have an otsu thresholding


## otsu thresholding
1. A more preferred way of thresholding, due to adaptivity and automatic selection of the threshold value
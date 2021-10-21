# image-gradients
1. Important when it comes to edge detection
1. It's a fundamental block of computer vision and image processing
1. Using image gradients helps us find contours and outlines of objects in an image(passport)
1. Edge detection relies on image gradient


## Edge detection vs Thresholding
1. Unlike thresholding that separates foreground from background
1. Edge detection highlights objects from background

## How it works
1. measures change in x direction and y direction of a given centered pixel
#### imagine that kernel

    1-*+y*-1

      |

    *-x*-1-*+x*

      |

    1--*-y*-1

#### same kernel logic, but instead of a normal convolution, we measure the difference in x and y axis and do this for every point, this way it gets very evident when neighboring pixels have a different value for edge detection

1. We need to calculate the gradient magnitude and gradient orientation.
1. Magnitude is calculated via Pythagorean theorem
1. To calculate them - We have Sobel Kernel and Scharr Kernel (which is a different variation of Sobel)

#### Sobel kernel for x

-1 0 +1

-2 0 +2

-1 0 +1

#### Sobel kernel for y

-1 -2 -1

0  0  0

+1 +2 +1

#### Use them the same way we use kernels, multiply everything and get the sum
#### Say we get 231 for x and 141 for y

magnitude = square root of 231 * 231 + 141 * 141 = 270.63

## Code

#### First argument is the image
#### Second argument is the ddepth. We usually use unsigned 8 bit integer because we want our values to be from 0 to 255
#### However Sobel kernel may give us a floating point, that's why we changed the ddepth, we'll convert it back to unsigned 8 bit integer before showing it to the screen
#### Third argument is dx, Fourth argument is dy, we need to select different ones as there are different Sobel kernels (for x and y)
#### Fourth argument is optional, needed when you want to use Scharr version
#### -1 is Scharr
#### 3 is Sobel
gX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=3)
gY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=3)

#### P.S both cv2.CV_32F and cv2.CV_64F are perfectly valid

### Convert back to an unsigned 8 bit integer
gX = cv2.convertScaleAbs(gX)
gY = cv2.convertScaleAbs(gY)
#### Again, we only convert so opencv can visualize them, because 0 to 255 are valid but 155.25 is not


### combine them
#### combine the gradient representations into a single image

#### first argument - image1
#### second argument - first weight
#### third argument - image2
#### fourth argument - second weight
#### fifth argument - gamma
combined = cv2.addWeighted(gX, 0.5, gY, 0.5, 0)
#### since we are combining 2 Sobel variations (x and y) we'd want to use the same weight for both of them
#### you can play with values by making a loop, but basicaly the lower that value is the darker the image is.
#### 0.5 is kinda in between
#### gamma, pretty much always keep at 0, and changing doesn't seem to be doing much

## When to use Scharr
1. when image is noisy

## How to add 2 images
combined = cv2.addWeighted(gX, 0.5, gY, 0.4, 0)

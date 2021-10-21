# edge-detectors
1. Utilizes image gradient
1. Canny edge detector is one most well known and most used edge detector
1. Can't get far without Canny edge detector in computer vision

## Why Canny and not image gradients?
1. While both achieve a similar result
1. Image gradient leaves us with a lot of noise
1. While Canny edge detector outputs a white edges and black blackground, 2 colors.

## Explanation
1. Canny edge detector takes the Soble edge detector and makes it a tiny bit better
1. Multi step algorithm
1. We first grayscale our image
1. Then blur it using Gaussian blur
1. Then use Soble edge detector for x and y coordinate
1. Calculate magnitude and orientation
1. Then we are ready for the Canny edge detection
    1.We don't want our edges to have much in them, we don't want bunch of pixels


## Non-maxima supression(thinning) - 3rd step
1. We examine gradient magnitude and orientation at each pixel in the image
1. Compare the current pixel to the 3x3 neighborhood surrounding it
1. Determine in which direction the orientation is pointing
1. Depending on the direction, examine magnitude of that orientation
1. If it's pointing somewhere on the y-axis, then examine north and south
1. If it's pointing somewhere on the x-axis, then examine east and west.
1. If center pixel magnitude is great than both pixels it's being compared to, then preserve the magnitude, otherwise, discard it.

### Example
1. We have a 255 pixel (white pixel identifying the top edge in the circle)
1. We compare that pixel to top and bottom, top is black (0) but bottom is 255, it's not greater than both so we discard that pixel
1. Examine the next pixel 255, top is black and bottom is black, so we keep the pixel.

## Hysteresis thresholding
1. After non-maxima supression, we may need to remove regions of an image that are technically not edges, but still respond as edges
1. We need to define 2 thresholds Tupper and Tlower
1. Any value that its higher than Tupper surely is an edge (probably don't make this bigger than 200, since white is 255)
1. Any values that is lower than Tlower surely is not an edge (so discard those pixels). If you make the value too high, it'd probably discard too much.
1. Good values (75,200)

### Example
1. *Point A* has a value of 225, our Tupper is 200, so *Point A* is safe
1. *Point B* has a value of 180, below our Tupper, but that Point is connected to *Point A* making it continuation of our edge.
1. *Point C* has a value of 150, below our Tupper and its not connected to anything, so we *discard* it
1. *Point D* has a value of 60, below our Tlower, *discard*

## Hard to find a right balance between upper and lower Threshold values

#### first argument image
#### second argument lower thresh
#### third argumetn upper threshold
test = cv2.Canny(blurred, 70, 200)

1. It's challenging to fine tune these values
1. The good advise is to start with these 3 and see where it feels closer
wide = cv2.Canny(blurred, 10, 200)
mid = cv2.Canny(blurred, 30, 150)
tight = cv2.Canny(blurred, 240, 250)

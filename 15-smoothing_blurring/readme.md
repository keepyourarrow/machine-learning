# smoothing_blurring

## Why blur an image?
1. Computers don't care about the HD super high quality image if anything it just confuses it even more.
1. We want the computer to detect a coffee cup in the hand, even a blurred coffee cup is still an object that can be detected.
1. Blurring an image makes it lighter, so it can be processed faster.
1. Reduces the amount of high-frequency content such as noise and edges.
1. In an object detection field, we want to detect edges of an image, and so it runs better and more precise, we would want to blur the stuff that are not important
1. Like when we are doing a 4-point transformation on the receipt, we don't want to see the content of the receipt, we just want to see the outline, the edges of it.
1. Or when we want to measure the distance between the object and the camera, we don't need to see the contents, so blurring can be used
1. Same logic with resizing an image.

## We can apply blurring and smoothing to any
1. grayscaled image
1. binary image
1. RGB image

## why are kernel sizes odd numbers (3,3) (5,5) (15,15)

#### so we have this concept of the centered pixel
#### make sure you don't overblur, make sure that kernel tuple isn't too high. Then that outline you wanted to see might mesh with the background
#### (15,15) seems too high. (7,7) on the other hand feels alright.


## blurring(simple)

### all pixels are equally important to calculate the average

#### that simple to blur
blurred = cv2.blur(image, (7, 7))
cv2.imshow("Title", blurred)

### how it works on a lower level

#### we have our 3x3 kernel
[
    [1,1,1],
    [1,1,1],
    [1,1,1]
]
#### and we have our part of the image that we apply that kernel to (also 3x3)
[
    [24,202,150],
    [50,75,90],
    [125,102,50]
]
#### we then apply that kernel, multiplying each number.

* 1x24
* 1x202
* 1x150
* 1x50
* 1x75
* 1x90
* 1x125
* 1x102
* 1x50
#### we get the same part of the image back since we multiplied by 1
[
    [24,202,150],
    [50,75,90],
    [125,102,50]
]
#### we then combine all those numbers
24 + 202 + 150 + 50 + 75 + 90 + 125 + 102 + 50 = 868
#### and get 868

#### we then divide it by 9
[[1,1,1],
[1,1,1],
[1,1,1]]
#### if we combine those we get 9

868 / 9 = 96.4
#### and that's by how much we are gonna blur the pixel in the center

## Gaussian blurring

#### center of the kernel has more weight
#### most of the time you'd be using this blur as opposed to normal one
#### it looks most natural to the human eye


#### same as the regular blur, but you also need to provide the last argument = 0
#### which basically tells cv2 to handle calculations.
blurred = cv2.GaussianBlur(image, (kX, kY), 0)

### how it works on a lower level

#### we have our 3x3 kernel
#### (in the Gaussian blur) we prioritize those in the center more, so it gets less blurry
[
    [1,2,1],
    [2,4,2],
    [1,2,1]
]
#### and we have our part of the image that we apply that kernel to (also 3x3)
[
    [24,202,150],
    [50,75,90],
    [125,102,50]
]
#### we then apply that kernel, multiplying each number.

* 1x24
* 2x202
* 1x150
* 2x50
* 4x75
* 2x90
* 1x125
* 2x102
* 1x50
#### we get the same part of the image back since we multiplied by 1
[
    [24,404,150],
    [100,300,180],
    [125,204,50]
]
#### we then combine all those numbers
24 + 404 + 150 + 100 + 325 + 180 + 125 + 204 + 50 = 1562
#### and get 1562

#### we then divide it by 16
[[1,2,1],
[2,4,2],
[1,2,1]]
#### if we combine those we get 16

868 / 9 = 96
#### and that's by how much we are gonna blur the pixel in the center

#### 0.4 smaller than a normal blur.
#### but keep in mind that the 3x3 kernel is arbitrary, as well as pixel colors in the image.

## NOTE
#### 96 is a new value we are gonna write in the center
[
    [24,202,150],
    [50,75,90],
    [125,102,50]
]

#### 75 is now 96

## Median blur
blurred = cv2.medianBlur(image, 7)


### When to use

* Is most effective when removing salt-and-pepper noise
* However, it's the worst blurring method to use on a normal image, since you can't really show it to a normal user, because of how unnatural it looks.

## lower level

#### our image grid
[
[128,140,115],
[140,255,140],
[115,133,155]
]

#### we grab the value in the middle (255) and replace it with a median

255,155,140,140,*140*,133,128,115,115
median = 140
#### new image grid
[
[128,140,115],
[140,140,140],
[115,133,155]
]

#### now imagine we did a regular blur
[
[128,140,115],
[140,255,140],
[115,133,155]
]
*
[
[1,1,1],
[1,1,1],
[1,1,1]
]
= 1321

1321 / 9 = 147

#### not quite 140 that we get from the median, but still surprisingly close. The result might be different with different points.

## Why median is more effective at removing salt-pepper noise
* Because the centered pixel is always replaced with a pixel intensity that exists in the image
* compared to the average
* the average pixel might not exist in our matrix grid, but the median always does.

## to calculate median you take the middle number
#### suppose we have
9, 1, 5, 250, 10, 2, 20
### first we order them
250, 20, 10, *9*, 5, 2, 1
#### 9 is our median

#### if its an even number
250, 20, 10, *15*, *9*, 5, 2, 1
(15 + 9) / 2 = 12
#### median = 12


## Salt-and-pepper noise

#### it looks similar to salt-and-pepper which is a noise that's present on some images make those very hard to look at.
#### Usually found in very old photos


## Bilateral blurring (filtering)

#### so far we've used blurring to reduce noise and detail in an image
#### but as a result we have tended to lose some edges in the image
### To reduce noise while still maintaining edges, we use Bilateral blurring.
### It does this by introducing 2 Gaussian distributions


#### second argument is similar to a kernel, the larger the diameter is, the more pixels will be included in the blurring computation
#### third argument is color deviation. The larger the value is, the more colors will be considered when computing the blur. If it's too large in respect to diameter, then we've essentially broken the assumption of bilateral filtering - that only pixels of similar color should contribute significantly to the blur
#### last argument is space deviation. A large value means that pixels farther out from the central pixel diameter will influence the blurring calculation
blurred = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)

#### example arguments
params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]


## lower level
* In simple words we use coordinates, just how we are used to using in other blurring methods(I think Gaussian)
* And in addition we also use pixel intensity, where only pixels of similar intensity is taken into considiration
* If pixels in the small neighborhood have a similar pixel intensity(value) then they likely represent a similar object
* However if two pixels in the same neighborhood have contrasting values, then it's likely a border or an edge, that we would like to preserve

## Downside to Bilateral blurring
#### It's considerably slower than its counterparts (Gaussian, median)
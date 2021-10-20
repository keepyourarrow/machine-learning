# colors

* Often overlooked in computer vision and processing
* I can guarantee you one thing that will never change. Computer vision depends on the quality of the images
* Lighting can mean the difference between success and failure of your computer vision algorithm.
* A camera doesn't film the object, instead it captures the light reflected off the object(help.png)
* A success of a computer vision program is determined way before any code is executed, by how well a picture is taken(lightning)



## When you work with lightning you want to obtain these 3 goals

1. High contrast (between your foreground and background)
    1.If you don't have high contrast you are gonna have a really hard time performing segmentation, thresholding, edge detection.
    1. Basically it'd be harder to detect the foreground (the object)
    1. So you gotta make sure there is a high contrast in the images you are working with
1. Generalizable
1. Stable
#### Generalizable, Stable is pretty hard to achieve. In different environments you might have different lightning
#### If you can ensure that pictures taken are in CONTROLLED environment, where you don't have to worry about the lightning, suddenly your job becomes much easier.
#### Example: factory?


## High contrast Goal

1. An object should have a relatively high contrast from the rest of the image so they are easily detectable
1. For example to make a document scanner we want a light document on a dark background, ensuring that the paper can be easily detected.

## Generalizable

1. Our lightning conditions should be generalizable enough to facilitate coin identification, whether we are examining a penny, a nickel or a dime.

## Stable

1. It's very important that we have a stable, consistent lightning
1. But often times its hard, especially if we are taking a picture outdoors. As time of the day changes, cloud rolls over the sun and rain starts to pour, our lightning conditions will change
1. The example with identifying the pills. Users from around the world would capture images under different lightning conditions. Outside, inside, and we simply have no control over it.
1. However if I were to do that in a factory or somewhere where I can control the camera and lightning, then suddenly we have a quite stable environment

## Color spaces
1. Just a specific organization of colors that allow us to consistently represent and reproduce colors
1. A geometric way of representing colors. On a x-y-z 3 dimensional coordinates, you plug the RGB values

## Color model
1. RGB
1. HSV
1. L* a * b *
1. Grayscale(not a colorspace, but we are gonna be using it a lot in our computer vision applications)

## Split channels
cv2.split(image)
#### will give us B G R individual channels

## Convert to HSV
#### very simple with cvtColor method.
#### notice how we call BGR2HSV, since we are converting from BGR
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#### splitting hsv channels is just as simple
cv2.split(hsv)

## Convert to lab
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
#### splitting lab is just as easy
cv2.split(lab)

## Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


## Why greyscale conversion are lit
* Every time we don't need colors, we can just throw them off -  less information to process

## HSV
#### Since plugging rgb values is counterintuitive, people have made a new way to pick the colors they want.
1. HSV is quite popular in computer vision, epsecially when we want to track the color of some object in an image
1. hue is how pure our color is. (BASICALLY A COLOR)
1. On the wheel, Hue is rotating the wheel to the desired color
1. Saturation - is an intensity of a color
1. Saturation - how white the color is, it's how red our red can be, counting from the center.
1. The centered red is black/gray, the further away from the center, the "redder" it is. The higher the saturation.

#### In the example. If we just select H channel, we'd have no colors
#### If we just select a Saturation channel, everything is black, because saturation is in the middle
#### If we select a Value channel, it looks like a greyscaled image because we removed the lightning


## LAB
1. Lightning
1. a-channel
1. b-channel

### a -channel
 1. defines pure red channel on one end of the a-channel spectrum and pure green on the other end
### b-channel
1. It's perpendicular to a-channel
1. On one end of the spectrum you have pure_yellow, on the other you have pure blue

###  kinda how it looks on the graph

                            pure_yellow
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
pure_green ---------------- center ------------------- pure_red
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                            pure blue

## Why to use LAB?
1. This is a color space/model where distance between colors actually matters.
1. view lab_help.png

## Grayscale
1. throws away all the information about the color


## Why grayscale images are not black and white images even though they are commonly refered to in that way
1. Grayscale images are single channel images with pixel values in *range* [0,255]
1. Black and white images(Binary images) can have *only two* possible values 0 or 255
1. Be careful not to refer to grayscale images as black and white images to avoid confusion as they are not really the same


## The formula to convert to grayscale

#### Interestingly enough, it's not
grayscale = 0.333 * R + 0.333 * G + 0.333 * B

#### because biologically our eyes are more sensitive to red and green than blue.
#### We notice 2x the amount of green than red and twice as much red as blue
#### so the formula is
grayscale = 0.299 * R + 0.587 * G + 0.114 * B

# Python

* zip - connect 2 lists,tuples
zip(("H", "S", "V"), cv2.split(hsv))
#### connected 2 tuples
zip(("H","S","V"), ("R","G","B"))
# opencv

##### each image has a number of pixels and those pixels can be manipulated(greyscaled), you can also decrease/increase those pixels

## pixels

##### Pixels are the building blocks of an image.
##### 600x450 image has 270,000 pixels.
##### Pixels are basically color blocks.
##### Pixels can represent a color or greyscale.
##### Greyscale has only 2 colors, black and white and only 1 channel.
##### represented by 2 numbers (0,255), the closer we are to 0 the darker the pixel is, the closer we are to 255 the lighter the pixel is

## rgb

##### represents how much of the color there is in the form of a tuple(red,green,blue)
**to get white, we fill all buckets with white (255,255,255)** - *because white is the presence of all colors*

**to get black, we fill all buckets with black (0,0,0)** - *because black is the absence of all colors*
##### to create red, we fill red and only red bucket (255, 0 ,0)

##### grab top left 0,0 coordinate rgb values.
##### the reason why its BGR and not RGB is because it used to be the standard way of doing it 20 years ago, back when OPENCV was first developed
##### it's a relic that stuck around, changing that would mean breaking all the other applications that have been built with opencv throughout those 20 years.
(b, g, r) = image[0,0]

##### always supply y and then x, height, then width.
##### because its number of rows(heigth) by number of columns(width)

##### you can update RGB values at any point
image[20,50] = (0, 0, 255)
##### at x=50, y=20 we want to update the RGB to red.
##### notice how its 0,0,255 not 255,0,0 because openCV reads BGR not RGB


## slicing an image
##### image is a numpy multidimensional array. first value accesses row, second accesses column.
##### image[row,column] #height,width
##### so if we supply image[height, width] we'd get the full image.
##### but if we want to slice it/crop it, we'd use numpy's slicing.
image[0:h, cX:w] # which would give us a top right corner

image[startY:endY, startX:endX]
(cX, cY) = (w // 2, h // 2)
##### cX,cY is half of the image, so basically we go from 0 to half for x and y
image[0:cX, 0:cY]


## tl,tr,bl,br
##### tl starts from 0,0 and stretches to half of height and half of width(very simple)
tl = image[0:cY, 0:cX]
##### tr y starts from 0 and stretches to half of height and x starts from half of width and stretches to total width(end of the image on x axis)
tr = image[0:cY, cX:w]
##### bl y starts from half of height and stretches to total height(end of the image on y axis), x starts from 0 and stretches to half of the width
bl = image[cY:h,0:cX]
##### br y starts from half of the height and stretches to total height(end of the image on y axis), x starts from half of the width and stretches to total width(end of the image on x axis)
br = image[cY:h,cX:w]



# python
## floor division

w // 2 # = 11 /2 = 5. 10 / 2 = 5

## slicing

lst = [6,7,8]
print(lst[0:2]) #would print 6,7
prnt(lst[-1]) #would print 8(last index)

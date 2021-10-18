# opencv lessons
image = cv2.imread('path to image')
image is a numpy array(a matrix of a bunch of numbers)

## we can get a shape of an image(3 is channels, what we usually work with)
image.shape[:3]

## show an image
cv2.imshow("title of the window", image)

## pause for user input, to do anything, like a click (before we write to a file)
cv2.waitKey(0)


#### height is a number of rows, width is a number of columns.
#### Think of an image as a table. there are 720 rows by 764 columns.

### channels 3 (rgb image)
# python lessons

## desctructuring(just like in js)
list = [764,720,3]
(w,h,c) = list
print(w)
#### instead of
print(list[0])


## printing via format
print("Width of our image: {}".format(w))
#### instead of
print("Width of our image:" + w)

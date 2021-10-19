# opencv

### you don't have to supply a preexisting image to use opencv, since image is just a multidimensional array of rows and columns you can create a working image, which is more proper to call a canvas by initializing it with numpy
canvas = np.zeros((300, 300, 3), dtype="uint8")
#### a canvas that's 300x300 with 3 channels (for rgb). It creates a multidimensional array with 300 rows, 300 columns and 3 values.
#### one row would look like this
[
    [0 0 0]
    [0 0 0]
    [0 0 0]
    ....
    #repeat 297 times
]
#### 0 represents black and np.zeros fills it with black values. since it's rgb, column has 3 values [0,0,0]
#### obviously once we change color it would be filled differently, like [202, 150, 255]

## draw line
### cv2.line(imageSource,from, to, color, thickness(optional))
cv2.line(canvas, (0, 0), (300, 300), (0, 255, 0))

### to draw a 3 pixel line
cv2.line(canvas, (300, 0), (0, 300), (0, 0, 255), 3)

## draw a rectangle
### cv2.rectangle(imageSource,topLeftCoordinates,BottomRightCoordinates, color, thickness(optional))
#### will be a wide rectangle 150X25
cv2.rectangle(canvas, (50,200),(200,225), (0,0,255), 5)

### filled rectangle
#### 25x75
cv2.rectangle(canvas,(200,50),(225,125),(255,0,0), -1)

## draw a circle
### cv2.circle(canvas, (centerX, centerY), radius, white, thickness)
cv2.circle(canvas, (centerX, centerY), 25, white, 2)
cv2.circle(canvas, (centerX, centerY), 25, white, -1) #filled circle

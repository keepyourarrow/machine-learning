# opencv

## image arithmetic
#### remember that the image is a matrix
#### when you substract 50 from the whole matrix, that huge numpy array, it will darken the image
#### likewise if you add 50 it will brighten the image

## clipping
#### max value is 255 and min value is 0 for our pixels

#### in the first example, we are trying to add 200 + 100 which will give us 300, but since 255 is max, we'll get 255
added = cv2.add(np.uint8([200]), np.uint8([100]))
#### in the second example we'd get -150, but since 0 is the minimum, then that's what we'll get
subtracted = cv2.subtract(np.uint8([50]), np.uint8([100]))
#### but that's only for cv2.subtract / cv2.add

#### we can do the same thing in numpy
#### instead of hitting the max value, numpy will do a wrap around
#### 254 => 255 => 0 => 1 => 2 .... => 43 => 44
#### in the first example we'll get 44
added = np.uint8([200]) + np.uint8([100])
#### in the second example we'll get 206
subtracted = np.uint8([50]) - np.uint8([100])

### What's important to understand is the wrap around concept
### these are 2 ways to subtract and add. numpy version may introduce some bugs in the code because it gives you a lot of freedom, while with cv2.subtract / cv2.add operations you are sure that cv2 will handle everything.


## how to brighten the image
#### we create an array filled with 1s (similar to how we made a canvas in #4-drawing where it was filled with 0s)
#### with the same shape as our original image. So if it's 900x900, it would be the same 900x900 but filled with 1s.
#### and we multiply it by a 100, which will make it a numpy array of 100s
M = np.ones(image.shape, dtype="uint8") * 100
#### then we use cv2.add method to combine 2 arrays. It will go over all the 900x900 rows x columns and add a 100 to it
added = cv2.add(image, M)

## how to darken the image

#### same concept as described above
M = np.ones(image.shape, dtype="uint8") * 50
subtracted = cv2.subtract(image, M)

* notice, that since we are using cv2.add / cv2.subtract methods if the value gets past 255 or 0, it will be clipped at that value, rather than wrapping around(a more preffered way) *

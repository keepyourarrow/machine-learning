# opencv

## resizing(preserve aspect ratio) for width

### we need to preserve the aspect ratio
### to calculate the ratio
### r = newWidth / oldWidth
r = 150.0 / width


### calculate dimensions
### first argument = newWidth. second argument = newHeight
dim = (150, int(height * r))  * if we don't multiply height by r, we keep it unchanged and don't preserve the aspect ratio
#### dim is a tuple where first value is the width that we want and second value is our old height multiplied by r and r is a small number like 0.5
#### say we have 200 height and 0.5 ratio, multiplying those two we get our new height = 100

## resizing(preserve aspect ratio) for height

### r = newHeight / oldHeight
r = 50.0 / height
### first argument = newHeight. second argument = newWidth
dim = (int(width * r), 50)  * if we don't multiply width by r, we keep it unchanged and don't preserve the aspect ratio

## resizing (with itumitls)

### it's a pain to do those aspect ratio calculations all the time, so as an alternative we can use imutils.resize method
resized = imutils.resize(image, width=100)
#### or for height
resized = imutils.resize(image, height=50)


## Why is it easier to resize from larger to smaller then vice versa?

#### because when you want to resize a larger image to a smaller one, you are just removing some of the pixels(data)
#### while to construct a larger image from a smaller one you have to basically add pixels that didn't exist there originally

## best ways to resize from a small image to a larger one.
#### by applying the interpolation parameter
#### the default one we used to convert from a large to a small one.
interpolation=cv2.INTER_AREA
interpolation=cv2.INTER_NEAREST)
interpolation=cv2.INTER_LINEAR)
# any of those are fine to use

#### good interpolations to convert a small image to a larger one
interpolation=cv2.INTER_CUBIC
interpolation=cv2.INTER_LANCZOS4
#### but mostly use CUBIC one, but the difference isn't the greatest.

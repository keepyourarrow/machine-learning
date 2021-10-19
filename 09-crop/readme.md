# opencv

## importance of slicing
#### make sure you know how to slice an array, its the easiest way to access different parts of an image without having to loop over it, which will take extra time and processing power

### see slicing.png


## roi
### roi = region of interest
roi = image[startY: endY, startX:endX]


# python

## more slicing

list = ['banana','orange','apple','bean','pear']

list[0:2] # *["banana","orange"]*
list[:2] # *["banana","orange"]*
list[2:4] # *["apple","bean"]*
list[2:] # *["apple","bean","pear"]*
list[:] # *["banana","orange","apple","bean","pear"]*
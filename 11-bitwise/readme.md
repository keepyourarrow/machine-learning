# opencv

### binary image = a simple image that has only white foreground and black background or vice versa. Only 2 colors

## bitwise operations

### incredibly important when it comes to masking and deep learning

#### to better understand the example, execute the script

### AND
#### when both values are true or false.
#### True True
#### False False
#### if you run the script, you could notice that it cuts off the rectangle parts that are not in the circle and circle parts that are not in the rectangle
bitwiseAnd = cv2.bitwise_and(rectangle, circle)

### OR
#### this will display corners of rectangle foreground that don't exist in the circle, and the corners of the circle foreground that don't exist in the rectangle
bitwiseOr = cv2.bitwise_or(rectangle, circle)

### XOR
#### only the value that don't exist are allowed. so the foreground where both shapes overlap aren't allowed an will instead be replaced with a background
bitwiseXor = cv2.bitwise_xor(rectangle, circle)


### NOT
#### it only accepts one shape and will foreground and background interchanging
bitwiseNot = cv2.bitwise_not(circle)

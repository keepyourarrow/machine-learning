# opencv

## masking

#### bitwise_and is used for masking

#### basically copy the original image's width and height and basically make a black canvas
mask = np.zeros(image.shape[:2], dtype="uint8")
#### then draw a rectangle on it
cv2.rectangle(mask, (0, 90), (290, 450), 255, -1)

#### we can now get a masked image, just that simple
masked = cv2.bitwise_and(image, image, mask=mask)

#### same can be done with a circle
mask = np.zeros(image.shape[:2], dtype="uint8")

cv2.circle(mask, (145, 200), 100, 255, -1)

masked = cv2.bitwise_and(image, image, mask=mask)

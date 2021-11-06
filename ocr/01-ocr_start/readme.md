# pytesseract
1. very simple
text = pytesseract.image_to_string(image)
1. Don't forget to convert BGR to RGB (as tesseract espects an image in RGB order)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

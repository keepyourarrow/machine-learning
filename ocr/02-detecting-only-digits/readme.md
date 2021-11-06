# detecting only digits(2)
1. It's possible to detect only digits

## How
1. Its simple, image_to_string accepts a second parameter called config
text = pytesseract.image_to_string(rgb, config="outputbase digits")

# correcting text orientation
1. We can get meta data from tesseract that will tell us how much the image is rotated, what kind of language it detected.
1. Those are very important when you don't know what you are working with, in order to correct it, before applying tesseract engine on it
1. Example: Making a web api that will take a document image and extract the text from it ( you'll need to auto rotate and stuff)
1. This way we don't need to apply any machine-learning ourself, all in all very useful tool in our toolbelt!
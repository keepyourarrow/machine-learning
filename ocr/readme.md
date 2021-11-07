#Basics of OCR
1. A series of algorithms and techniques that try to capture the text
1. It's hard to achieve a 100% accuracy as many factors are involved in the OCR, but our goal is to get as close to 100% as possible
1. OCR is pretty incredible when it comes to blind people or people with reading disabilities.

## Different type of OCR
1. There are softwares
1. Actual tools like - Digital pen, a pen that scans the text as you go over it word by word.

## It's extremely challenging
1. There are different handwritings, different fonts
1. Text in the document can be damaged, noisy, very hard for a machine to read

## Apps to make
1. Automatic license plate recognition
1. Analyzing and defeating CAPTCHAs
1. Extract VISA card information
1. Passport
1. A photo translator app (show an image and tesseract will detect the language and translate it)

# What can we do
1. It's possible to detect only digits
1. It's possible to whitelist, blacklist
1. Extract meta data and correct it (rotate it, get language information etc) - very important for document detection

# PSM options
1. --psm 0 *to extract meta information*
1. --psm 1 *ignore(not working correctly)*
1. --psm 2 *ignore(not implemented by tesseract)*
1. --psm 3 *the default one*
1. --psm 4 *use it when you want have data lined up as a column (receipt)*
1. --psm 5 *ignore, useless*
1. --psm 6 *good to scan book pages* **NOTE: that its assumed that text is uniform (same font without any variation, and books usually have that) bold or italic text at times is fine**
1. --psm 7 *single line of text(very useful) default mode might not detect single lines at all or as well as mode 7 can*
1. --psm 8 *single word(can be used interchangeably with --psm 7 )*
1. --psm 9 *ignore (circular segmentation)*
1. --psm 10 *single character*
1. --psm 11 *very good when there's a lot of text and you don't particularly care about the order(would probably be good to use for that extract text from the photo app)*
1. --psm 12 *ignore*
1. --psm 13 *its good for single lines only, use it as a last resort when nothing else works (would be nice to read a weird font)*

# PSM tips
1. Try using the default mode first and see the result
1. Try using --psm 13 more often, because it would work more times than not
1. Consider first running a --psm 0 to find out the confidence level in the script, if not, then just let the user know.
# detecting low contrast
1. If you need to tell user that the image is too low contrast

#### one fraction does the job
#### you'd probably need to tune the fraction_threshold.
is_low_contrast(gray, fraction_threshold=0.35):
## how it determines low contrast or not
1. If pixels aren't spreat out much

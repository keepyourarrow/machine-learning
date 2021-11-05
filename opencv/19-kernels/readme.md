# kernels

## Why odd kernels

1. because it has a clear center

#### a 3x3 kernel
1-1-1

1-*1*-1

1-1-1

#### a 2x2 kernel

1-1

1-1
#### no center

## convolutions
1. you take 2 matrices and multiply every number by its respecting neighbor and then add them up, that simple
1. say we have this 2 arrays
1. a = [
    1. [0,1,2],
    1. [3,4,5],
    1. [6,7,8]
    1. ]
1. b = [
    1. [0,1,2],
    1. [3,4,5],
    1. [6,7,8]
    1. ]
1. now multiply them (a * b)
1. we get
1. [
    1. [0,1,4],
    1. [9,16,25],
    1. [36,49,64]
    1. ]
1. then we add those up and get 204
#### full formula
(a * b).sum()
#### that simple

## P.S im dumb convolution is literally what we have done in morphological operations and smoothing_blurring, using a structuring element/kernel

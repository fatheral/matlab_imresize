# imresize test
Here the test script and input data are located.
## Test procedure
Input image (`lena_512x512.png`) was resized by MatLab's `imresize` in two different ways: as an uint8 image and as a double image with values from interval [0,1]. These two options were tested as the most widespread among DL-scientists. Also, MatLab's `imresize` behaves differently (in terms of clipping its values) for uint8 and double data types (it doesn't clip the values when dealing with doubles, it does clipping when saving image on disk by `imwrite`).

The produced images are:
```
lena_123x234_uint8.png
lena_123x234_double.png
```
The MatLab code for producing these images is the following:
```matlab
img_uint8 = imread('lena_512x512.png');
img_double = double(img_uint8) / 255;
new_size = [123, 234];

new_img_uint8 = imresize(img_uint8, new_size);
imwrite(new_img_uint8, 'lena_123x234_uint8.png');

new_img_double = imresize(img_double, new_size);
imwrite(new_img_double, 'lena_123x234_double.png');
``` 
## Supposed output
The output of the script `test_imresize.py` should be the following (at least for MatLab R2015b):
```
Python/MatLab uint8 diff: min = 0 max = 0
Python/Matlab double diff: min = 0 max = 0
```
It shows max/min differences between uint8 images produced by Python's and its MatLab's origin `imresize` function.

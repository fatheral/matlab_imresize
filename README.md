# matlab_imresize
Python implementation of MatLab imresize() function.

## Table of contents
1. [Background](#background)
2. [System requirements](#req)
3. [Usage](#usage)
4. [Additional info](#addinfo)
5. [Note](#note)
## Background <a name="background"></a>
In the latest Super Resolution challenges (e.g. see [NTIRE 2017](http://www.vision.ee.ethz.ch/ntire17/)) the downscaling - *bicubic interpolation* - is performed via MatLab imresize() function.

[Track info](http://www.vision.ee.ethz.ch/ntire17/#challenge):
> Track 1: bicubic  uses the **bicubic downscaling (Matlab imresize)**, one of the most common settings from the recent single-image super-resolution literature.

[More info](https://competitions.codalab.org/competitions/16303):
> For obtaining the low res images we use the **Matlab function "imresize" with default settings (bicubic interpolation)** and the desired downscaling factors: 2, 3, and 4.

Moreover, the quality (PSNR) of a tested solution is compared with the reference solution - upsampling with bicubic interpolation - which is done again with MatLab imresize() function with the default settings.

All this leads to:
1. Preparing train database (downscaling High-Resolution images) using MatLab
2. Reference solution (upscaling with bicubic interpolation) is also should be done using MatLab

As the most of the Deep Learning code is written under the python, we need to do some additional preprocessing/postprocessing using completely different environment (MatLab), and can't do upscaling/downscaling in-place using simple python functions. As a result, the implemented python imresize() function is done to overcome these difficulties.
## System requirements <a name="req"></a>
* python 2.7
* numpy
## Usage <a name="usage"></a>
imresize of *uint8* image using scale (e.g. 0.5 or 2):
```python
Img_out = imresize(Img_in, scalar_scale=0.333) # Img_out of type uint8
```
imresize of *uint8* image using shape (e.g. (100, 200)):
```python
Img_out = imresize(Img_in, output_shape=(123, 324)) # Img_out of type uint8
```
Above examples are working when input image `Img_in` is of the type **uint8**. But often the image processing is done in **float64**, and converted to uint8 only before saving on disk. The following code is for obtaining the same result as doing *imresize+imwrite* in MatLab for input image of doubles:
```python
import numpy as np
from skimage.io import imsave, imread
from skimage import img_as_float
img_uint8 = imread('test.png')
img_double = img_as_float(img_uint8)
new_img_double = imresize(img_double, output_shape=(123, 324)
imsave('test_double.png', convertDouble2Byte(new_img_double))
```
## Additional information <a name="addinfo"></a>
Actually, the implemented python code was made by re-writing MatLab code `toolbox/images/images/imresize.m`, and it can't be done without brilliant insight made by [S. Sheen](https://stackoverflow.com/users/6073407/s-sheen) about how `imresizemex` can be implemented (originally, it is binary provided with MatLab distribution): [stackoverflow](https://stackoverflow.com/questions/36047357/what-does-imresizemex-do-in-matlab-imresize-function).

In fact, if you have **OpenCV** and have the ability to re-compile it, probably the best solution is to change parameter `A` inside function `interpolateCubic`, which is located (at least for release 3.2.0) on line `3129` inside file `opencv-3.2.0/modules/imgproc/src/imgwarp.cpp`, from *-0.75f* to *-0.5f* (the value used in MatLab). Then simply use function `cv::resize` from OpenCV. For more information please refer to [stackoverflow](https://stackoverflow.com/questions/26823140/imresize-trying-to-understand-the-bicubic-interpolation). Also, see [another stackoverflow answer](https://stackoverflow.com/questions/29958670/how-to-use-matlabs-imresize-in-python) about different ways of resizing the image inside python.
## Note <a name="note"></a>
Please note that no optimization (aside from preliminary numpy-based vectorizing) was made, so the code can be (and it is) times slower than the original MatLab code.

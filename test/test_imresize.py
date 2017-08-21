import numpy as np
from skimage.io import imsave, imread
from skimage import img_as_float
import sys
sys.path.append('..')
from imresize import *

# 1. Load original image and do imresize+save both im UINT8 and FLOAT64 types
img_uint8 = imread('lena_512x512.png')
new_size = (123, 234)
new_img_uint8 = imresize(img_uint8, output_shape=new_size)
imsave('py_lena_123x234_uint8.png', new_img_uint8)
img_double = img_as_float(img_uint8)
new_img_double = imresize(img_double, output_shape=new_size)
imsave('py_lena_123x234_double.png', convertDouble2Byte(new_img_double))

# 2. Load images resized by python's imresize() and compare with images resized by MatLab's imresize()
matlab_uint8 = imread('lena_123x234_uint8.png')
python_uint8 = imread('py_lena_123x234_uint8.png')
matlab_double = imread('lena_123x234_double.png')
python_double = imread('py_lena_123x234_double.png')
diff_uint8 = matlab_uint8.astype(np.int32) - python_uint8.astype(np.int32)
diff_double = matlab_double.astype(np.int32) - python_double.astype(np.int32)
print 'Python/MatLab uint8 diff: min =', np.amin(diff_uint8), 'max =', np.amax(diff_uint8)
print 'Python/Matlab double diff: min =', np.amin(diff_double), 'max =', np.amax(diff_double)

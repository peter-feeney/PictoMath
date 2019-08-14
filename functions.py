'''


Style Suggestion: Each function takes a matrix and the rest of the image processing is done outside function.

(e.g. functions only handle matrices)

'''
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as im
from numpy.linalg import inv
from numpy.linalg import svd

def add(img_mat1, img_mat2):
    return img_mat1 + img_mat2

'''
Given img_path, resizes an image to 300 x 300
An additional param can be added to control image size, but 300 x 300 is good for now
'''
def im_resize(img_path):
    img = Image.open(img_path)
    return img.resize((300, 300))

def svd(img_mat):
    return svd(img_mat)
'''
Displays the transpose (90 degree flip)
given the matrix corresponding to the image
'''
def transpose(img_mat):
    img_mat = np.rot90(img_mat, k = -1)
    img = Image.fromarray(img_mat)
    img.show()

def scalar_mult(img_mat, scalar):
    return scalar * img_mat

def shear(img_mat, scalar):

'''
This function is redundant, but computes the inverse of a matrix
'''
def inverse(img_array):
    return inv(img_array)

'''
Given img_path, resizes an image to 300 x 300
An additional param can be added to control image size, 
but 300 x 300 is good for now
'''
def im_resize(img_path):
    img = Image.open(img_path)
    return img.resize((300, 300))

def img_mult(img1, img2):
    image1 = im_resize(img1)
    image2 = im_resize(img2)

    img_mat1 = np.asarray(image1, dtype=np.uint8)
    img_mat2 = np.asarray(image2, dtype=np.uint8)
    print(img_mat1)

    img_product = img_mat1 * img_mat2
    print(img_product)

    pic = Image.fromarray(img_product)
    pic.show()

#Testing with some of old social media profile pictures
#I got interesting results by multiplying an image by itself.
img_mult('C:/Users/peter/Pictures/facebookprofile.jpg','C:/Users/peter/Pictures/profilePic.jpg')
img_mult('C:/Users/peter/Pictures/profilePic.jpg','C:/Users/peter/Pictures/profilePic.jpg')













'''
All of this code is random testing stuff. One key fact to remember
is how to obtain the RGB slices of an image, which you can do like this

img_mat[:, :, x] where x is in between 0 and 2 inclusive

Also you can do scalar multiplication and abs() easily
'''
image = im_resize('C:/Users/egypt/PycharmProjects/PictoMath/img.jpg')
img_mat = np.asarray(image, dtype=np.uint8)
transpose(img_mat)
pic = Image.fromarray(img_mat[:, :, 0])
print(img_mat.shape)
img_inv_1 = inv(img_mat[:, :, 0])
img_inv_2 = inv(img_mat[:, :, 1])
img_inv_3 = inv(img_mat[:, :, 2])

img_ma = np.zeros((300, 300, 3), 'uint8')

mult_constant = 256
img_ma[:, :, 0] = img_inv_1 * mult_constant
img_ma[:, :, 1] = img_inv_2 * mult_constant
img_ma[:, :, 2] = img_inv_3 * mult_constant

pic = Image.fromarray(img_ma)
pic.show()



pic = Image.fromarray(10000 * img_inv)

'''
picture = Image.fromarray((img_mat[:, :, 0]))
picture.show()
pic = Image.fromarray(img_mat)
#pic.show()
picture = Image.fromarray((img_array[:, :, 0]))
#picture.show()
picture = Image.fromarray((img_array[:, :, 1]))
#picture.show()
picture = Image.fromarray(inv(img_array[:, :, 2]))
#picture.show()

'''
'''
import statements

Dependencies: (Use pip install x)

pillow
numpy
matplotlib


'''
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as im
from numpy.linalg import inv


'''
Given img_path, resizes an image to 300 x 300
An additional param can be added to control image size, but 300 x 300 is good for now
'''
def im_resize(img_path):
    img = Image.open(img_path)
    return img.resize((300, 300))


'''
Displays the transpose (90 degree flip)
given the matrix corresponding to the image
'''
def transpose(img_mat):
    img_mat = np.rot90(img_mat, k = -1)
    img = Image.fromarray(img_mat)
    img.show()

'''
This function is redundant, but computes the inverse of a matrix
'''
def inverse(img_array):
    return inv(img_array)



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
# coding: utf-8
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as im
from numpy.linalg import inv

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




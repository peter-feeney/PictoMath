from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

def im_preprocess():
    img_path = 'C:/users/egypt/Desktop/image.jpg'
    img = Image.open(img_path)
    img_resized = img
    return img_resized


def transpose(img):
    flip = img.transpose(Image.FLIP_LEFT_RIGHT)
    flip.show()


image = im_preprocess()
transpose(image)





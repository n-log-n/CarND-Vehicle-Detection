import numpy as np
import cv2
import glob
import random

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

from setup import fetch_data

from features import get_hog_features
from features import extract_features
from features import extract_feature

from search_and_classify import *

# fetch_data()

car_imgs = glob.glob('./data/vehicles/*/*.png')
noncar_imgs = glob.glob('./data/non-vehicles/*/*.png')

idx1 = np.random.randint(len(car_imgs))
idx2 = np.random.randint(len(noncar_imgs))


car = mpimg.imread(car_imgs[idx1])
plt.imshow(car)
plt.savefig('output_images/car1.jpg')

noncar = mpimg.imread(noncar_imgs[idx2])
plt.imshow(noncar)
plt.savefig('output_images/noncar1.jpg')

colorspace = 'YCrCb' # Can be RGB, HSV, LUV, HLS, YUV, YCrCb
orient = 9
pix_per_cell = 8
cell_per_block = 2
hog_channel = 'ALL'


# hog_features, hog_img = get_hog_features(car[:, :, 0], orient, pix_per_cell, cell_per_block, vis=True)
# plt.imshow(hog_img, cmap='gray')
# plt.savefig('output_images/car1_hog.jpg')

# hog_features, hog_img = get_hog_features(noncar[:, :, 0], orient, pix_per_cell, cell_per_block, vis=True)
# plt.imshow(hog_img, cmap='gray')
# plt.savefig('output_images/noncar1_hog.jpg')

features = extract_feature(car, colorspace, orient, pix_per_cell, cell_per_block, hog_channel)
print (features.shape)
import cv2
import numpy as np

# euclidean and isometic
# affine
# projective transforms

# 1) GEOMETRIC TRANSFORMATION
# Transformation is modifying spatial relationship between pixels
# 2) image can be shifted,rotated ans streched in multiple ways

# --> Euclidean and Isometric transform:
# Whenever an image is shifted(translation) in x or y axis or rotated is euclidean or isometric transform
# Euclidean transform is a subset of affine transform
#      -- R is an orthogonal matrix
#      -- Euclidean distance is preserved
#      -- Has three degrees of freedom, two for translation and one for rotation
#      -- Characterstics include: Distance, Angles and Shaped remains preserved


# load the image 
img = cv2.imread('linkedinDP.jpg')

# Translation matrix
matrix = np.float32([[1,0,100], [0,1,100]])

# apply matrix to the image, affine  is generalisation of euclidean transformation
translated = cv2.warpAffine(img, matrix, (img.shape[1]+100, img.shape[0]+100))


# Affine transformation
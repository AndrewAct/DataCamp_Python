# # 8/14/2020
# In this exercise, you will apply unsupervised segmentation to the same image, before it's passed to a face detection machine learning model.

# So you will reduce this image from 265×191=50,615 pixels down to 400 regions.

# Import the slic function from segmentation module
from skimage.segmentation import slic

# Import the label2rgb function from color module
from skimage.color import label2rgb

# Obtain the segmentation with 400 regions
segments = slic(face_image, n_segments= 400)

# Put segments on top of original image to compare
segmented_image = label2rgb(segments, face_image, kind='avg')

# Show the segmented image
show_image(segmented_image, "Segmented image, 400 superpixels")
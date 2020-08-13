# # 8/12/2020
# In this exercise, we'll try to reduce the noise of a thresholded image using the dilation morphological operation.


# Import the module
from skimage import morphology

# Obtain the dilated image 
dilated_image = morphology.binary_dilation(world_image)

# See results
show_image(world_image, 'Original')
show_image(dilated_image, 'Dilated image')
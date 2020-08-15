# # 8/14/2020
# In this exercise we'll find the contour of a horse.

# For that we will make use of a binarized image provided by scikit-image in its data module. Binarized images are easier to process when finding contours with this algorithm. Remember that contour finding only supports 2D image arrays.

# Once the contour is detected, we will display it together with the original image. That way we can check if our analysis was correct!

# show_image_contour(image, contours) is a preloaded function that displays the image with all contours found using Matplotlib.

# Import the modules
from skimage import data, measure

# Obtain the horse image
horse_image = data.horse()

# Find the contours with a constant level value of 0.8
contours = measure.find_contours(horse_image, 0.8)

# Shows the image with contours found
show_image_contour(horse_image, contours)
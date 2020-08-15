# # 8/14/2020
# In this exercise you will identify the shapes in a grapefruit image by detecting the edges, using the Canny algorithm.

# canny filer is a multi-stage edge detector
# It uses a filter based on the derivative of a Gaussian in order to compute the intensity of the gradients
# Import the canny edge detector 
from skimage.feature import canny

# Convert image to grayscale
grapefruit = color.rgb2gray(grapefruit)

# Apply canny edge detector
canny_edges = canny(grapefruit)

# Show resulting image
show_image(canny_edges, "Edges with Canny")
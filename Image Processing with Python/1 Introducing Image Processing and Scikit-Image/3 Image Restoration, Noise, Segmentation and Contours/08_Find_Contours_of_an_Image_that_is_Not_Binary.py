# # 8/14/2020
# Let's work a bit more on how to prepare an image to be able to find its contours and extract information from it.

# We'll process an image of two purple dices loaded as image_dices and determine what number was rolled for each dice.

# In this case, the image is not grayscale or binary yet. This means we need to perform some image pre-processing steps before looking for the contours. First, we'll transform the image to a 2D array grayscale image and next apply thresholding. Finally, the contours are displayed together with the original image.

# color, measure and filters modules are already imported so you can use the functions to find contours and apply thresholding.

# We also import io module to load the image_dices from local memory, using imread. Read more here.

# Make the image grayscale
image_dices = color.rgb2gray(image_dices)

# Obtain the optimal thresh value
thresh = filters.threshold_otsu(image_dices)

# Apply thresholding
binary = image_dices > thresh

# Find contours at a constant value of 0.8
contours = measure.find_contours(binary, 0.8)

# Show the image
show_image_contour(image_dices, contours)
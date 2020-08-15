# # 8/14/2020
# Now we have found the contours, we can extract information from it.

# In the previous exercise, we prepared a purple dices image to find its contours:

# This time we'll determine what number was rolled for the dice, by counting the dots in the image.

# The contours found in the previous exercise are preloaded as contours.

# Create a list with all contour's shapes as shape_contours. You can see all the contours shapes by calling shape_contours in the console, once you have created it.

# Check that most of the contours aren't bigger in size than 50. If you count them, they are the exact number of dots in the image.

# show_image_contour(image, contours) is a preloaded function that displays the image with all contours found using Matplotlib.

# Create list with the shape of each contour
shape_contours = [cnt.shape[0] for cnt in contours]

# Set 50 as the maximum size of the dots shape
max_dots_shape = 50

# Count dots in contours excluding bigger than dots size
dots_contours = [cnt for cnt in contours if np.shape(cnt)[0] < max_dots_shape]

# Shows all contours found 
show_image_contour(binary, contours)

# Print the dice's number
print("Dice's dots number: {}. ".format(len(dots_contours)))

# <script.py> output:
#     Dice's dots number: 9.

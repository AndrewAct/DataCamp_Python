# # 8/12/2020
# We want to downscale the images of a veterinary blog website so all of them have the same compressed size.

# It's important that you do this proportionally, meaning that these are not distorted.

# First, you'll try it out for one image so you know what code to test later in the rest of the pictures.

# Import the module and function
from skimage.transform import resize

# Set proportional height so its half its size
height = int(dogs_banner.shape[0] / 2)
width = int(dogs_banner.shape[1] / 2)

# Resize using the calculated proportional height and width
image_resized = resize(dogs_banner, (height, width),
                       anti_aliasing=True)

# Show the original and rotated image
show_image(dogs_banner, 'Original')
show_image(image_resized, 'Resized image')
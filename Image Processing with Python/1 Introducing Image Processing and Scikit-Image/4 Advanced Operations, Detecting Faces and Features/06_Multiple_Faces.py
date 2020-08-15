# # 8/14/2020
# In this exercise, you will detect multiple faces in an image and show them individually. Think of this as a way to create a dataset of your own friends' faces!

# The Cascade of classifiers class from feature module has already been imported, as well as the show_detected_face() function which is used to display the face marked in the image and crop it so it can be shown separately.

# Load the trained file from data
trained_file = data.lbp_frontal_face_cascade_filename()

# Initialize the detector cascade
detector = Cascade(trained_file)

# Detect faces with scale factor to 1.2 and step ratio to 1
detected = detector.detect_multi_scale(img=friends_image,
                                       scale_factor=1.2,
                                       step_ratio=1,
                                       min_size=(10, 10),
                                       max_size=(200, 200))
# Show the detected faces
show_detected_face(friends_image, detected)

# <script.py> output:
#     {'r': 218, 'c': 440, 'width': 52, 'height': 52}
#     {'r': 207, 'c': 152, 'width': 47, 'height': 47}
#     {'r': 219, 'c': 533, 'width': 48, 'height': 48}
#     {'r': 202, 'c': 402, 'width': 45, 'height': 45}
#     {'r': 217, 'c': 311, 'width': 39, 'height': 39}
#     {'r': 202, 'c': 31, 'width': 36, 'height': 36}
#     {'r': 242, 'c': 237, 'width': 41, 'height': 41}
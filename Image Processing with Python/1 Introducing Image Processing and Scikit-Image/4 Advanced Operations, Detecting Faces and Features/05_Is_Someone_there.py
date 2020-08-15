# # 8/14/2020
# In this exercise, you will check whether or not there is a person present in an image taken at night.

# The Cascade of classifiers class from feature module has been already imported. The same is true for the show_detected_face() function, that is used to display the face marked in the image and crop so it can be shown separately.


# From the official website:
# The main idea behind cascade of classifiers is to creat classifiers of meidum accuracy 
# and em=nsemble them into one strong classifier instead just creating a strong one
# Load the trained file from data
trained_file = data.lbp_frontal_face_cascade_filename()

# Initialize the detector cascade
detector = Cascade(trained_file)

# Detect faces with min and max size of searching window
detected = detector.detect_multi_scale(img = night_image,
                                       scale_factor=1.2,
                                       step_ratio=1,
                                       min_size=(10, 10),
                                       max_size=(200, 200))

# Show the detected faces
show_detected_face(night_image, detected)


# <script.py> output:
#     {'r': 774, 'c': 131, 'width': 40, 'height': 40}

# 5/17/2020
# Import necessary modules
from sklearn import datasets
import matplotlib.pyplot as plt

# Load the digits dataset: digits
digits = datasets.load_digits()

# Print the keys and DESCR of the dataset
print(digits.keys())
print(digits.DESCR)

# Print the shape of the images and data keys
print(digits.images.shape)
print(digits.data.shape)

# Display digit 1010
plt.imshow(digits.images[1010], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()

# <script.py> output:
#     dict_keys(['data', 'target', 'target_names', 'images', 'DESCR'])
#     Optical Recognition of Handwritten Digits Data Set
#     ===================================================
    
#     Notes
#     -----
#     Data Set Characteristics:
#         :Number of Instances: 5620
#         :Number of Attributes: 64
#         :Attribute Information: 8x8 image of integer pixels in the range 0..16.
#         :Missing Attribute Values: None
#         :Creator: E. Alpaydin (alpaydin '@' boun.edu.tr)
#         :Date: July; 1998
    
#     This is a copy of the test set of the UCI ML hand-written digits datasets
#     http://archive.ics.uci.edu/ml/datasets/Optical+Recognition+of+Handwritten+Digits
    
#     The data set contains images of hand-written digits: 10 classes where
#     each class refers to a digit.
    
#     Preprocessing programs made available by NIST were used to extract
#     normalized bitmaps of handwritten digits from a preprinted form. From a
#     total of 43 people, 30 contributed to the training set and different 13
#     to the test set. 32x32 bitmaps are divided into nonoverlapping blocks of
#     4x4 and the number of on pixels are counted in each block. This generates
#     an input matrix of 8x8 where each element is an integer in the range
#     0..16. This reduces dimensionality and gives invariance to small
#     distortions.
    
#     For info on NIST preprocessing routines, see M. D. Garris, J. L. Blue, G.
#     T. Candela, D. L. Dimmick, J. Geist, P. J. Grother, S. A. Janet, and C.
#     L. Wilson, NIST Form-Based Handprint Recognition System, NISTIR 5469,
#     1994.
    
#     References
#     ----------
#       - C. Kaynak (1995) Methods of Combining Multiple Classifiers and Their
#         Applications to Handwritten Digit Recognition, MSc Thesis, Institute of
#         Graduate Studies in Science and Engineering, Bogazici University.
#       - E. Alpaydin, C. Kaynak (1998) Cascading Classifiers, Kybernetika.
#       - Ken Tang and Ponnuthurai N. Suganthan and Xi Yao and A. Kai Qin.
#         Linear dimensionalityreduction using relevance weighted LDA. School of
#         Electrical and Electronic Engineering Nanyang Technological University.
#         2005.
#       - Claudio Gentile. A New Approximate Maximal Margin Classification
#         Algorithm. NIPS. 2000.
    
#     (1797, 8, 8)
#     (1797, 64)
import numpy as np
import cv2


def preprocess_image(img):
    # Convert the image to a NumPy array
    img_array = np.array(img)
    # Convert to grayscale
    gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
    # Resize the image
    resized = cv2.resize(gray, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
    # Apply adaptive thresholding
    processed_image = cv2.adaptiveThreshold(
        resized,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        61,
        11
    )

    return processed_image

#line 1 - NumPy is a popular library in Python used for numerical computing. It provides support for large multidimensional arrays and matrices, 
#         along with a collection of mathematical functions to operate on these arrays.
#line 2 - The line imports OpenCV, a widely used library for real-time computer vision tasks, offering functionalities for image and video processing.
#line 5 - This line defines a function named preprocess_image that takes one argument img. This function is designed to preprocess an input image.
#line 7 - This line converts the input image img into a NumPy array, essential for compatibility with many OpenCV functions.
#line 9 - This line converts the image from BGR (Blue-Green-Red) to grayscale.
#line 11 - This line resizes the grayscale image gray to 1.5 times its original dimensions.
#          'gray' - It represents the input image for resizing. 
#          'None' - The output size is determined automatically based on the scaling factors.
#          'fx' and 'fy' - Here, the image is scaled to 1.5 times its original size in both dimensions. 
#          'cv2.INTER_LINEAR' chosen ensures bilinear interpolation for resizing, ideal for maintaining image quality.
#Adaptive Thresholding - In image processing, adaptive thresholding is a method that can handle changing lighting conditions. 
#                        It is used to separate desirable foreground image objects from the background based on the difference in pixel intensities of each region.
#           0 represents black, and 255 represents white.
#line 13 - 'resized' - The input image to be thresholded.
#           '255' - The maximum intensity value that can be assigned to a pixel.
#           'cv2.ADAPTIVE_THRESH_GAUSSIAN_C' - It indicates that the threshold value is calculated as the weighted sum of neighborhood values, where weights are a Gaussian window.
#           'cv2.THRESH_BINARY' - It means that pixels with intensities higher than the threshold value are set to the maximum value (255), and others are set to 0.
#           '61' - The size of the local region (block size) used for adaptive thresholding. It must be an odd number.
#           '11' - Constant subtracted from the calculated mean or weighted mean.
#line 22 - This line returns the processed image, which is the result of the preprocessing steps applied within the preprocess_image() function.

# Typically, a file named util.py serves as a container for utility functions or helper classes that are used across different modules or scripts within a project. 
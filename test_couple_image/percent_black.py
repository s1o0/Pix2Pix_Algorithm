import cv2
import numpy as np

def percent_black_pixels(path_to_image):
    # reading the image data from desired directory
    img = cv2.imread(path_to_image)
    #cv2.imshow('Image',img)
    
    # counting the number of pixels
    number_of_white_pix = np.sum(img == 255)
    number_of_black_pix = np.sum(img == 0)

    number_of_pixels = img.shape[0]*img.shape[1]*img.shape[2]

    '''print('Number of white pixels:', number_of_white_pix)
    print('Number of black pixels:', number_of_black_pix)
    print('Number of pixels:', number_of_pixels)
    print('Percentage of black pixels:', number_of_black_pix*100/number_of_pixels)'''
    return number_of_black_pix*100/number_of_pixels

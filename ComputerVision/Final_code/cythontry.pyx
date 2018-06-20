import cv2
import cython
import numpy as np@cython.boundscheck(False)
cpdef double[:, :,:] threshold_fast(int T, float[:, :,:] image, double[:, :,:] image1):
   # set the variable extension types
   cdef int x, y, w, h, x1, z
   cdef double start,temp
   #cv2.imshow('newimage',image)
   # grab the image dimensions
   h = image.shape[0]
   w = image.shape[1]
   # loop over the image
   for y in range(0, h):
           for x in range(0,w):
               temp = (image[y][x][0] + image[y][x][1] + image[y][x][2])/3.0
               if(temp < T and temp > -1*T):
                   image1[y][x][0] = 0
                   image1[y][x][1] = 0
                   image1[y][x][2] = 0
               elif(temp > 0):
                   image1[y][x][0] = 255
                   image1[y][x][1] = 0
                   image1[y][x][2] = 0
               elif(temp < 0):
                   image1[y][x][0] = 0
                   image1[y][x][1] = 255
                   image1[y][x][2] = 0
               else:
                   image1[y][x][0] = 0
                   image1[y][x][1] = 0
                   image1[y][x][2] = 255
   # return the thresholded image
   return image1
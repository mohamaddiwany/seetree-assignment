from flask import render_template
import numpy as np

class imagestat:
    #Function to check the min of the pic
    def minimum(self,stat,IMAGE_FILE_NAME):
        return [x[0] for x in stat.extrema]
    #Function to check the max of the pic
    def maximum(self,stat,IMAGE_FILE_NAME):
        return [x[1] for x in stat.extrema]
    #Function to check the mean of the pic
    def mean(self,stat,IMAGE_FILE_NAME):
        return stat.mean
    #Function to check the median of the pic
    def median(self,stat,IMAGE_FILE_NAME):
        return stat.median
    #Function to check the percentile of the pic
    def percentile(self,img,IMAGE_FILE_NAME,FUNC_NAME):
        pixels = list(img.getdata())
        return np.percentile(pixels,int(FUNC_NAME[1:]))

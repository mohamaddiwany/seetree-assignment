from flask import render_template
import numpy as np

class imagestat:
    #Function to check the min of the pic
    def minimum(self,stat,IMAGE_FILE_NAME):
        mynew = [x[0] for x in stat.extrema]
        return render_template("index3.html", user_image = "local-filename.jpg" ,IMG_NAME= IMAGE_FILE_NAME , value = mynew , text =' Min values for each band in the image is')
    #Function to check the max of the pic
    def maximum(self,stat,IMAGE_FILE_NAME):
        mynew = [x[1] for x in stat.extrema]
        return render_template("index3.html", user_image = "local-filename.jpg" ,IMG_NAME= IMAGE_FILE_NAME , value = mynew , text =' Max values for each band in the image is')
    #Function to check the mean of the pic
    def mean(self,stat,IMAGE_FILE_NAME):
        mynew = stat.mean
        return render_template("index3.html", user_image = "local-filename.jpg" ,IMG_NAME= IMAGE_FILE_NAME ,value = mynew , text ='Average (arithmetic mean) pixel level for each band in the image is')
    #Function to check the median of the pic
    def median(self,stat,IMAGE_FILE_NAME):
        mynew = stat.median
        return render_template("index3.html", user_image = "local-filename.jpg" ,IMG_NAME= IMAGE_FILE_NAME ,value = mynew , text =' Median pixel level for each band in the image is')
    #Function to check the percentile of the pic
    def percentile(self,img,IMAGE_FILE_NAME,FUNC_NAME):
        pixels = list(img.getdata())
        mynew = np.percentile(pixels,int(FUNC_NAME[1:]))
        return render_template("index3.html", user_image = "local-filename.jpg" ,IMG_NAME= IMAGE_FILE_NAME ,value = mynew , text =' {} percentile of the image is'.format(FUNC_NAME[1:]))
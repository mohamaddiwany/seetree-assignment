# importing all the packages which is neccesarry for work
from flask import Flask, render_template, request,Response , redirect , url_for 
import requests
from PIL import Image , ImageStat
import urllib.request
import numpy as np
import imagestat as istat
import time
app = Flask(__name__)


image_data_dict = {}
#the main route 127.0.0.1:5000
@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

#the route where you can find all the name of pic which function
@app.route('/index1.html', methods=['GET'])
def home():
    return render_template('index1.html')

#the route which respone a 200 status_code
@app.route('/health')
def starting_url():
    # status_code = Response(status=200)
    return render_template("index2.html"),200

#the route where all the work are done
@app.route('/stats/<IMAGE_FILE_NAME>/<FUNC_NAME>')
def starting_work(IMAGE_FILE_NAME,FUNC_NAME):
    start_time = time.time()
    min_message = ' Min values for each band in the image is'
    max_message = ' Max values for each band in the image is'
    median_message = 'Average (arithmetic mean) pixel level for each band in the image is'
    mean_message = ' Median pixel level for each band in the image is'
    percintle_message = ' {} percentile of the image is'.format(FUNC_NAME[1:])

    if IMAGE_FILE_NAME in image_data_dict:
            if FUNC_NAME in image_data_dict[IMAGE_FILE_NAME]:
                if FUNC_NAME == 'min':
                    message = min_message
                if FUNC_NAME == 'max':
                    message = max_message
                if FUNC_NAME == 'median':
                    message = median_message
                if FUNC_NAME == 'mean':
                    message = mean_message
                if FUNC_NAME[0] == 'p':
                    message = percintle_message
                
                elapsed_time = time.time() - start_time
                
                return render_template("index3.html", user_image = "local-filename.jpg" ,IMG_NAME= IMAGE_FILE_NAME , value = image_data_dict[IMAGE_FILE_NAME][FUNC_NAME] , text =message ,elapsedtime=elapsed_time)
    #Make Sure the FUNC_NAME is one of the supported function
    if FUNC_NAME != 'min' and FUNC_NAME != 'max' and FUNC_NAME != 'mean' and FUNC_NAME != 'median':
        if FUNC_NAME[0] !='p' or  not FUNC_NAME[1:].isnumeric() or int(FUNC_NAME[1:])< 0 or int(FUNC_NAME[1:]) >100:
            # return Response(status=404)
            return render_template("index4.html"),404
    
    #get the picture
    url = "https://storage.googleapis.com/seetree-demo-open/{}".format(IMAGE_FILE_NAME)

    #try to open it if it exist or had open permission
    try:
        urllib.request.urlretrieve(url, "local-filename.jpg")
    except Exception :
        return render_template("index5.html"),404
    
    # save the img localy
    img = Image.open("local-filename.jpg")

    #run ImageStat to get all the stats for the Image
    stat = ImageStat.Stat(img)
    #check which function is needed to work and return the correct answer
    if FUNC_NAME == 'min':
        image_data_dict[IMAGE_FILE_NAME]={}
        image_data_dict[IMAGE_FILE_NAME][FUNC_NAME] = istat.imagestat.minimum(istat,stat,IMAGE_FILE_NAME)
        elapsed_time = time.time() - start_time
        return render_template("index3.html", user_image = "local-filename.jpg" ,IMG_NAME= IMAGE_FILE_NAME , value = image_data_dict[IMAGE_FILE_NAME][FUNC_NAME] , text =min_message,elapsedtime=elapsed_time)


    if FUNC_NAME == 'max':
        image_data_dict[IMAGE_FILE_NAME]={}
        image_data_dict[IMAGE_FILE_NAME][FUNC_NAME] = istat.imagestat.maximum(istat,stat,IMAGE_FILE_NAME)
        elapsed_time = time.time() - start_time
        return render_template("index3.html", user_image = "local-filename.jpg" ,IMG_NAME= IMAGE_FILE_NAME , value = image_data_dict[IMAGE_FILE_NAME][FUNC_NAME] , text =max_message,elapsedtime=elapsed_time)


    if FUNC_NAME == 'mean':
        image_data_dict[IMAGE_FILE_NAME]={}
        image_data_dict[IMAGE_FILE_NAME][FUNC_NAME] = istat.imagestat.mean(istat,stat,IMAGE_FILE_NAME)
        elapsed_time = time.time() - start_time
        return render_template("index3.html", user_image = "local-filename.jpg" ,IMG_NAME= IMAGE_FILE_NAME , value = image_data_dict[IMAGE_FILE_NAME][FUNC_NAME] , text =mean_message,elapsedtime=elapsed_time)
        
    if FUNC_NAME == 'median':
        image_data_dict[IMAGE_FILE_NAME]={}
        image_data_dict[IMAGE_FILE_NAME][FUNC_NAME] = istat.imagestat.median(istat,stat,IMAGE_FILE_NAME)
        elapsed_time = time.time() - start_time
        return render_template("index3.html", user_image = "local-filename.jpg" ,IMG_NAME= IMAGE_FILE_NAME , value = image_data_dict[IMAGE_FILE_NAME][FUNC_NAME] , text =median_message,elapsedtime=elapsed_time)

    if FUNC_NAME[0] == 'p':
        image_data_dict[IMAGE_FILE_NAME]={}
        image_data_dict[IMAGE_FILE_NAME][FUNC_NAME] = istat.imagestat.percentile(istat,img,IMAGE_FILE_NAME,FUNC_NAME)
        elapsed_time = time.time() - start_time
        return render_template("index3.html", user_image = "local-filename.jpg" ,IMG_NAME= IMAGE_FILE_NAME , value = image_data_dict[IMAGE_FILE_NAME][FUNC_NAME] , text =percintle_message,elapsedtime=elapsed_time)
        

#If we run it using seetree.py not throw flask we get it on port 80
if __name__ == "__main__":
    app.run(debug=True , host="0.0.0.0" , port=5000)
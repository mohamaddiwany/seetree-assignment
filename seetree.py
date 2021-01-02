# importing all the packages which is neccesarry for work
from flask import Flask, render_template, request,Response , redirect , url_for 
import requests
from PIL import Image , ImageStat
import urllib.request
import numpy as np
app = Flask(__name__)

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
    return render_template("index2.html")

#the route where all the work are done
@app.route('/stats/<IMAGE_FILE_NAME>/<FUNC_NAME>')
def starting_work(IMAGE_FILE_NAME,FUNC_NAME):

    #Make Sure the FUNC_NAME is one of the supported function
    if FUNC_NAME != 'min' and FUNC_NAME != 'max' and FUNC_NAME != 'mean' and FUNC_NAME != 'median':
        if FUNC_NAME[0] !='p' or  not FUNC_NAME[1:].isnumeric() or int(FUNC_NAME[1:])< 0 or int(FUNC_NAME[1:]) >100:
            return Response(status=404)
            # return render_template("index4.html")
    
    #get the picture
    url = "https://storage.googleapis.com/seetree-demo-open/{}".format(IMAGE_FILE_NAME)

    #try to open it if it exist or had open permission
    try:
        urllib.request.urlretrieve(url, "local-filename.jpg")
    except Exception :
        return Response(status=404)
        # return render_template("index4.html")
    
    # save the img localy
    img = Image.open("local-filename.jpg")

    #run ImageStat to get all the stats for the Image
    stat = ImageStat.Stat(img)

    #check which function is needed to work and return the correct answer
    if FUNC_NAME == 'min':
        mynew = [x[0] for x in stat.extrema]
        return render_template("index3.html",value = mynew , text =' Min values for each band in the image is')
    if FUNC_NAME == 'max':
        mynew = [x[1] for x in stat.extrema]
        return render_template("index3.html",value = mynew , text =' Max values for each band in the image is')
    if FUNC_NAME == 'mean':
        mynew = stat.mean
        return render_template("index3.html",value = mynew , text ='Average (arithmetic mean) pixel level for each band in the image is')
    if FUNC_NAME == 'median':
        mynew = stat.median
        return render_template("index3.html",value = mynew , text =' Median pixel level for each band in the image is')
    if FUNC_NAME[0] == 'p':
        pixels = list(img.getdata())
        mynew = np.percentile(pixels,int(FUNC_NAME[1:]))
        return render_template("index3.html",value = mynew , text =' the {} percentile of the image is'.format(FUNC_NAME[1:]))

#If we run it using seetree.py not throw flask we get it on port 80
if __name__ == "__main__":
    app.run(debug=True , host="127.0.0.1" , port=80)

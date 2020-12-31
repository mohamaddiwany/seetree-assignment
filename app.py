from flask import Flask, render_template, request,Response
import requests
import json
from PIL import Image , ImageStat
import urllib.request
import numpy as np
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():

    return "Welcome to my home"


@app.route('/health')
def starting_url():
    status_code = Response(status=200)
    return status_code

@app.route('/stats/<IMAGE_FILE_NAME>/<FUNC_NAME>')
def starting_work(IMAGE_FILE_NAME,FUNC_NAME):
    # if IMAGE_FILE_NAME[:4] != 'IMG_' or IMAGE_FILE_NAME[-4:] != '.jpg' or not IMAGE_FILE_NAME[4:-4].isnumeric() or \
    #     int(IMAGE_FILE_NAME[4:-4])<1 or int(IMAGE_FILE_NAME[4:-4]) > 10:
    #     return Response(status=404)

    if FUNC_NAME != 'min' and FUNC_NAME != 'max' and FUNC_NAME != 'mean' and FUNC_NAME != 'median':
        if FUNC_NAME[0] !='p' or  not FUNC_NAME[1:].isnumeric() or int(FUNC_NAME[1:])< 0 or int(FUNC_NAME[1:]) >100:
            return Response(status=404)
    url = "https://storage.googleapis.com/seetree-demo-open/{}".format(IMAGE_FILE_NAME)
    try:
        urllib.request.urlretrieve(url, "local-filename.jpg")
    except Exception :
        return Response(status=404)
    img = Image.open("local-filename.jpg")
    stat = ImageStat.Stat(img)
    if FUNC_NAME == 'min':
        mynew = [x[0] for x in stat.extrema]
    if FUNC_NAME == 'max':
        mynew = [x[1] for x in stat.extrema]
    if FUNC_NAME == 'mean':
        mynew = stat.mean
    if FUNC_NAME == 'median':
        mynew = stat.median
    if FUNC_NAME[0] == 'p':
        pixels = list(img.getdata())
        mynew = np.percentile(pixels,int(FUNC_NAME[1:]))
    return'Hi,{}'.format(mynew)

    

if __name__ == "__main__":
    app.run(debug=True , host="0.0.0.0" , port=80)
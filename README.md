# Seetree Home Assignment
Image statistics are common features in AI applications.
In the following assignment we are implemented a web server that handles
calculation of image statistics. For example, given an image we would like to calculate the
min,max,mean values etc

## Common setup
Clone the repo and install the dependencies.
```bash
git clone https://github.com/mohamaddiwany/seetree-homework.git
```

## Usage - By Flask

open Command Prompt and go to the file location then tap 
```bash
py -m pip install -r requirements.txt
set FLASK_APP=seetree.py
flask run
```
## Usage - By Docker

open Command Prompt and go to the file location then tap
```bash
docker build -t seetree .
```
that's will build the docker image for you then tap
```bash
docker run -d -p 80:80 seetree
```
## Work
Go over the [localhost](https://127.0.0.0:5000) with port 5000 because flask run with that port
From there you can go to home page and navigate by choosing pictures and functions or use the url
/health: will respond with “OK” to any request
/stats/IMAGE_FILE_NAME/FUNC_NAME : will calculate FUNC_NAME on the
pixels of given IMAGE_FILE_NAME and return the result. Supported
FUNC_NAMES should be:
i. min
ii. max
iii. mean
iv. median
v. pXXX where XXX is a percentile between 0...100. For example p10 is the
10th percentile of the image, p99 is the 99th percentile
All the images that should be supported are stored in a bucket named :
seetree-demo-open .
Currently there are 10 images in this bucket named IMG_1.jpg, IMG_2.jpg …
IMG_10.jpg. 

## Examples
a. Request to /stats/IMG_1.jpg/min should respond with the correct min value in the
image
b. Request to /stats/IMG_1.jpg/average should respond with 404 error code
c. Request to /stats/IMG_100.jpg/min should respond with 404 error code
(assuming such image was not added to the bucket)



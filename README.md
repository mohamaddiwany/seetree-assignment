# Seetree Home Assignment
Image statistics are common features in AI applications.
In the following assignment we are implemented a web server that handles
calculation of image statistics. For example, given an image we would like to calculate the
min,max,mean values etc

## Common setup
Clone the repo and install the dependencies.
```bash
git clone https://github.com/mohamaddiwany/seetree-assignment.git
```

## Usage - By Flask

open Command Prompt and go to the file location then tap 
```bash
py -m pip install -r requirements.txt
set FLASK_APP=seetree.py
flask run
```
Go over the [localhost](https://127.0.0.0:5000) with port 5000 because flask run with that port

## Usage - By Docker

open Command Prompt and go to the file location then tap
```bash
docker build -t seetree .
```
that's will build the docker image for you then tap
notice: a docker demon must be running before building the image
```bash
docker run -d -p 5000:5000 seetree
```
Go over the [localhost](https://127.0.0.0:5000)
## Work

/health : will respond with “OK” to any request

/stats/IMAGE_FILE_NAME/FUNC_NAME : will calculate FUNC_NAME on the
pixels of given IMAGE_FILE_NAME and return the result.
Supported FUNC_NAMES should be:

i. min

ii. max

iii. mean

iv. median

v. pXXX where XXX is a percentile between 0...100. For example p10 is the
10th percentile of the image, p99 is the 99th percentile.

All the images that should be supported are stored in a bucket named :
seetree-demo-open .
Currently there are 10 images in this bucket named IMG_1.jpg, IMG_2.jpg …
IMG_10.jpg. 

## Extra
You can open the [localhost](https://127.0.0.0:5000) , there you can see 
a site with seetree video on it , besides a links to my social media accounts
if you select the home button then it will navigate to a site where you can 
choose which picture you want to work on and which function you want to apply
I didn't put a button for percintle function because i would use post to get which number the put after p while we should only use get

## What you should know about functions
I choose to returns the value which display three bands for that you will have three answers for some method , I could transform the picture to grayscale but then I think I lost the Imagestats for RGB image cause in real world we have RGB pictures rather than grayscales which we used to have in the past 

## Examples
a. Request to /stats/IMG_1.jpg/min should respond with the correct min value in the
image.

b. Request to /stats/IMG_1.jpg/average should respond with 404 error code.

c. Request to /stats/IMG_100.jpg/min should respond with 404 error code
(assuming such image was not added to the bucket).


## Bonus :
I made a dictionary that save the Images data , this would help if i go another time to check the same image , i don't have to wait until all the image processing done and that will save our time

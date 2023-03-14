
# Import Libraries
from serpapi import GoogleSearch
import os
import urllib.request

# Google Parameters
google_params = {
      "q": "Cute Cats", # ------- Mention Search Query here
      "tbm": "isch",
      "api_key": "  ------------- API KEY -----------------   "
    }

# Get the Response and Fetch the links
response = GoogleSearch(google_params)
results = response.get_dict()
images_list = results['images_results']

images_links = []
for image in images_list:
    images_links.append(image['original'])

# Code to download the images
def download_google_images(images_links):

    for i in range(len(images_links)):
        basepath = r" ---------- PATH WHERE YOU WANT YOUR IMAGES ---------------  "
        try:
            name = "" + str(i) + ".png"
            basepath = os.path.join(basepath,name)
            urllib.request.urlretrieve(images_links[i], basepath)
        except Exception as e:
            print("error for ",e)
            pass

download_google_images(images_links)

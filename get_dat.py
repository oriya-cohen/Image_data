!pip install wget
import os, sys, wget
from zipfile import ZipFile

# data from : https://homes.cs.washington.edu/~ranjay/visualgenome/api.html
# we need only the images - not the rest of the data as we will do auto encoding prosses
url_dat = ['https://cs.stanford.edu/people/rak248/VG_100K_2/images.zip'
      'https://cs.stanford.edu/people/rak248/VG_100K_2/images2.zip']

for w_path in url_dat:
  wget.download(w_path, out =  os.getcwd())
for file in os.listdir(os.getcwd()):
    if file.endswith(".zip"):
        zip = ZipFile(file)
        zip.extractall()
    else:
        print("not found")


      

# with the help from : 
# https://stackoverflow.com/questions/66288078/any-easy-way-to-get-imagenet-dataset-for-training-custom-model-in-tensorflow

import io
import urllib
import os
import
from PIL import Image

def saveFromURL(url, path):
    img_file = io.BytesIO(urllib.request.urlopen(url).read())
    Image.open(img_file).save(path)

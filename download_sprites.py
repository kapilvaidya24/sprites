

import re
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from PIL import Image

def get_valid_filename(s):
    s = str(s).strip().replace(' ', '_')
    return re.sub(r'(?u)[^-\w.]', '', s)

# MAIN SITE TO DOWNLOAD SPRITES FROM
site = 'https://www.spriters-resource.com/search/?q=mario'

# SITE TO APPEND IMG URL 
site1= 'https://www.spriters-resource.com'

response = requests.get(site)

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')

urls = [img['src'] for img in img_tags]
stuff = [(img['src'], img['alt']) for img in img_tags]




for stuff_point in tqdm(stuff):
    url=stuff_point[0] 
    # NEEDED TO REMOVE SPACES FROM FILENAME TO SUIT WINDOWS
    filename=get_valid_filename(stuff_point[1])   
    if "ario" not in filename and "ARIO" not in filename:
        continue 
    if not filename:
         print("Regex didn't match with the url: {}".format(url))
         continue
    with open("/mnt/c/Users/aditi/sprite_download/mario/"+filename+".png", 'wb+') as f:
        if 'http' not in url:
            # sometimes an image source can be relative 
            # if it is provide the base url which also happens 
            # to be the site variable atm. 
            url = '{}{}'.format(site1, url)
        response = requests.get(url)
        f.write(response.content)

        # ### ADDS WHITE BACKGROUND TO TRANSPARENT SPRITES
        # file_exact_name="/mnt/c/Users/aditi/sprite_download/mario/"+filename+".png"
        # try:
        #     im = Image.open(file_exact_name)
        # except IOError:
        #     print("Error with: "+file_exact_name)
        #     continue        
        # # BACKGROUND COLOR CODE        
        # fill_color = (255,255,255)  # your new background color

        # im = im.convert("RGBA")   # it had mode P after DL it from OP
        # if im.mode in ('RGBA', 'LA'):
        #     background = Image.new(im.mode[:-1], im.size, fill_color)
        #     background.paste(im, im.split()[-1]) # omit transparency
        #     im = background

        # im.convert("RGB").save(file_exact_name) 




### This script needs to run later than downloading code as images 
### might not get fully downloaded immediately after the request is sent

### ADDS WHITE BACKGROUND TO TRANSPARENT SPRITES
import os
list_filename=[]
for filename in os.listdir("mario/"):
    if filename.endswith(".png"): 
        list_filename.append(filename)


from PIL import Image

for file in list_filename:
        file_exact_name="mario/"+file
        try:
        	im = Image.open(file_exact_name)
        except IOError:
	        print("Error with"+file_exact_name)
	        continue        
        # BACKGROUND COLOR CODE        
        fill_color = (255,255,255)  # your new background color

        im = im.convert("RGBA")   # it had mode P after DL it from OP
        if im.mode in ('RGBA', 'LA'):
            background = Image.new(im.mode[:-1], im.size, fill_color)
            background.paste(im, im.split()[-1]) # omit transparency
            im = background

        im.convert("RGB").save(file_exact_name)        
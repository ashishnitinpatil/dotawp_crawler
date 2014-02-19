# Rename the downloaded images with the actual titles!
import os
import json

img_dir = os.path.join(os.getcwd(), 'images\\full')
items = json.load(open(os.path.join(os.getcwd(), 'data.json'), 'r'))
for item in items:
    if len(item['images']) > 0:
        cur_file = item['images'][0]['path'].split('/')[-1]
        cur_format = cur_file.split('.')[-1]
        new_title = item['title']+'.%s'%cur_format
        file_path = os.path.join(img_dir, cur_file)
        os.rename(file_path, os.path.join(img_dir, new_title))

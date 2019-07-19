import os
import hashlib
import json
from PIL import Image
from shutil import copyfile

sprite_template = """
    {
        "name": "[SPRITE_NAME]",
        "md5": "x[HASH].[EXT]",
        "type": "sprite",
        "json": {
            "objName": "[SPRITE_NAME]",
            "costumes": [
                {
                    "costumeName": "[COSTUME_NAME]",
                    "baseLayerID": -1,
                    "baseLayerMD5": "x[HASH].[EXT]",
                    "bitmapResolution": 2,
                    "rotationCenterX": [HALF_WIDTH],
                    "rotationCenterY": [HALF_HEIGHT]
                }
            ],
            "currentCostumeIndex": 0,
            "scratchX": 0,
            "scratchY": 0,
            "scale": 1,
            "direction": 90,
            "rotationStyle": "normal",
            "isDraggable": false,
            "visible": true,
            "spriteInfo": {}
        }
    }"""

all_the_sprites = "["

for file in os.listdir('./images'):

    if file.startswith('.'):
        continue

    filepath = './images/' + file;
    print (filepath)
    
    # file info
    sprite_name = file[:-4]
    file_ext = file[-4:]
    file = open(filepath,'rb');
    md5 = hashlib.md5(file.read()).hexdigest()
    hash_ext = md5 + file_ext;

    # image info
    img = Image.open(filepath)
    width, height = img.size

    # write new file
    copyfile(filepath, '../static/assets/x'+hash_ext)

    # fill up json
    this_sprite = sprite_template \
        .replace("[SPRITE_NAME]", sprite_name) \
        .replace("[HASH].[EXT]", hash_ext) \
        .replace("[COSTUME_NAME]", sprite_name.lower()) \
        .replace("[HALF_WIDTH]", str(int(width/2))) \
        .replace("[HALF_HEIGHT]", str(int(height/2)))
    
    # add to list
    all_the_sprites += this_sprite + ","

# remove last comma and close the json array
all_the_sprites = all_the_sprites[:-1] + "\n]"
#print(json.dumps(all_the_sprites));

# print to json file
json_file = open('../src/lib/libraries/sprites.json', 'w+')
json_file.write(all_the_sprites)
json_file.close()



    




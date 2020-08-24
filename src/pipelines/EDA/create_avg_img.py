import numpy as np
from PIL import Image
import os, sys

path = '../../../data/img/img_dumps/'
save_adopted_path = '../../../data/img/adopted/'
save_adoptable_path = '../../../data/img/adoptable/'
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if 'DS_Store' not in item: #mac issue
            if os.path.isfile(path+item):
                im = Image.open(path+item)
                file, e = os.path.splitext(path+item)
                imResize = im.resize((450, 450), Image.ANTIALIAS)
                # imResize.save(file + '_resized.jpg', 'JPEG', quality=90)
                imResize.save(save_adopted_path + item + '_resized.jpg', 'JPEG', quality=90)



if __name__ == '__main__':
    
    
    resize()

   
import numpy as np
from PIL import Image
import os, sys

path = '../../../data/img/img_dumps/'
save_adopted_path = '../../../data/img/adopted/'
save_adoptable_path = '../../../data/img/adoptable/'
dirs = os.listdir( path )

def resize():
    # breakpoint()
    for item in dirs:
        if 'DS_Store' not in item:
            if os.path.isfile(path+item):
                im = Image.open(path+item)
                file, e = os.path.splitext(path+item)
                imResize = im.resize((450, 450), Image.ANTIALIAS)
                # breakpoint()
                # imResize.save(file + '_resized.jpg', 'JPEG', quality=90)
                imResize.save(save_adopted_path + item + '_resized.jpg', 'JPEG', quality=90)



if __name__ == '__main__':
    
    resize()


    # # Access all jpg files in directory
    # allfiles=os.listdir(os.getcwd())
    # imlist=[filename for filename in allfiles if  filename[-4:] in [".jpg",".PNG"]]

    # # Assuming all images are the same size, get dimensions of first image
    # w,h=Image.open(imlist[0]).size
    # N=len(imlist)

    # # Create a np array of floats to store the average (assume RGB images)
    # arr=np.zeros((h,w,3),np.float)

    # # Build up average pixel intensities, casting each image as an array of floats
    # for im in imlist:
    #     imarr=np.array(Image.open(im),dtype=np.float)
    #     arr=arr+imarr/N

    # # Round values in array and cast as 8-bit integer
    # arr=np.array(np.round(arr),dtype=np.uint8)

    # # Generate, save and preview final image
    # out=Image.fromarray(arr,mode="RGB")
    # out.save("average_dog_img.png")
    # out.show()
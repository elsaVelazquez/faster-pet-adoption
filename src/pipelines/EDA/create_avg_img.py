import numpy as np
from PIL import Image
import os, sys

'''heavily borrwed from stack overflow'''
adopted_path = '../../../data/img/adopted/'
adoptable_path = '../../../data/img/adoptable/'


if __name__ == '__main__':
    

    status = adoptable_path #to easily toggle between adopted and adoptable
    
    all_files=os.listdir(status)
    #sanity checks
    # print(all_files)
    # print(all_files[0])

    # all images are the same size, getting dimensions of first image
    w,h=Image.open(status + all_files[0]).size
    N=len(all_files)

    # to store the average (assume RGB images)
    arr=np.zeros((h,w,3),np.float)

    # # Build up average pixel intensities
    for im in all_files:
        if 'DS_Store' not in im: #to get around Mac-specific issue
            imarr=np.array(Image.open(status + im),dtype=np.float) #each image cast as an array of floats
            arr=arr+imarr/N

    # Round values in array and cast as 8-bit integer
    arr=np.array(np.round(arr),dtype=np.uint8)

    # Generate, save and preview final image
    out=Image.fromarray(arr,mode="RGB")
    out.save("average_dog_img.png")
    out.show()
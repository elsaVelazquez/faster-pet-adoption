from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import glob
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_curve
from sklearn.metrics import f1_score, confusion_matrix, balanced_accuracy_score
from sklearn.metrics import classification_report, mean_squared_error, r2_score
import numpy as np
from sklearn.model_selection import KFold
from skimage.io import imread
from skimage.transform import resize
from skimage.color import rgb2gray
import os


from random import seed
from random import randrange

def open_images(path):
    train_images = imread(path)
    gray_image = rgb2gray(train_images) #makes image gray scale
    gray_size = resize(gray_image, (32, 32))
    grey_ravel = gray_size.ravel()
    return grey_ravel

def make_X_y():
    X = []
    y = []   
    dog_ids = []

    #the [:5] is for testing and when subset is smaller, remobe the [:-1] at ~line 49
    all_images = os.listdir('../../../data/img/img_dumps/')#[:5]

    for dog_pic_label in all_images:
        path = glob.glob('../../../data/img/img_dumps/*.jpg')#[:5]
        label = (dog_pic_label)
        if 'adoptable' in label:
            label = 0
        # if 'adopted' in label:  
        else:
            label = 1
        y.append(label)

               
    for p in path:                
        X.append(open_images(p))
        dog_ids.append(dog_pic_label) #this is for keeping track of the dogs if necessary     

    X = np.asarray(X)
    y = np.asarray(y)[:-1] #the [:-1] compensates for an extra appended in y, otherwise data aligns
    # print("length X: ", len(X))
    # print("length y: ", len(y))
    # print("all images: ", all_images)
    # print(y)
    # print(X)
    print("X, y, and all_images made")
    return X, y, all_images

   
if __name__ == '__main__':
    # root_mean = rmse(y_true, y_predict)
    X, y, all_images = make_X_y()



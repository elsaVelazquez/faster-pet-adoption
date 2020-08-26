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
# from make_X_y import *


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

    all_images = os.listdir('../../../data/img/img_dumps/') #[:10]

    for dog_pic_label in all_images:
        path = glob.glob('../../../data/img/img_dumps/*.jpg') #[:10]
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
    # print("these got misclassified: ")
    # print(dog_ids[0])
    # print(X)
    print("X, y and all_images made")
    return X, y, all_images


# def naive_bayes():
#     X, y, all_images = make_X_y()
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)    
    
#     model = MultinomialNB()
#     model.fit(X_train, y_train)
#     y_pred = model.predict(X_test)
#     #the next two prints are to see where the miscassification ocurred
#     print(y_pred)
#     print(y_test)
#     acc = accuracy_score(y_test, y_pred)
#     print("The following indeces did not predict accurately: ")
    
#     #hard coded for now
#     # print(all_images[0])
#     # print(all_images[1])
#     # print(all_images[6])
#     # print(all_images[7])
#     # print(all_images[9])
#     # print(all_images[13])
#     # print(all_images[15])
#     # print(all_images[16])
#     # print(all_images[18])
#     # print(all_images[20])
#     # print(all_images[21])
    
#     print("Naive Bayes Accuracy: ", acc)
    
#     return acc, y_pred, y_test, all_images

    
if __name__ == '__main__':
    # root_mean = rmse(y_true, y_predict)
    X, y, all_images = make_X_y()
    # naive_bayes_acc, y_pred, y_test, all_images = naive_bayes()
    
    # Naive Bayes Accuracy:  0.6384180790960452


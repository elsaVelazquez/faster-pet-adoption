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
from make_X_y import *


def naive_bayes():
    X, y, all_images = make_X_y()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)    
    
    model = MultinomialNB()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    return acc, y_pred, y_test, all_images

    
if __name__ == '__main__':
    
    X, y, all_images = make_X_y()
    naive_bayes_acc, y_pred, y_test, all_images = naive_bayes()
    
# Naive Bayes Accuracy:  0.6136363636363636


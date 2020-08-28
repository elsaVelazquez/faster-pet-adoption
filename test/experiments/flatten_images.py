

#small dataset feature selection
from skimage.io import imread
from skimage.transform import resize
from skimage.color import rgb2gray
import os



def open_images(path):
    train_images = imread(path)
    gray_image = rgb2gray(train_images) #for making image gray scale
    # color_size = resize(train_images, (50, 50))
    gray_size = resize(gray_image, (32, 32))
    gray_ravel = gray_size.ravel()
    return gray_ravel


dog_pics_directory = os.listdir('../../../data/img/img_dumps')[:2]
# print(dog_pics_directory)
path = '../../../data/img/img_dumps/'

# for folder in data_folders:
import pandas as pd
import numpy as np

data = pd.DataFrame([])
for dog_pic in dog_pics_directory:
    # image = imread(r"../../../data/img/img_dumps/48549555_adoptable.jpg")
    # print(dog_pic)
    # print(path + dog_pic )
    # print(dog_pics_directory)
    full_path = path + dog_pic 
    # print(full_path)
    # img = "../../../data/img/img_dumps/48554156_adoptable.jpg"
    # print(img)
    list_ravel = []
    if dog_pic == dog_pic:
        image_initial = imread(full_path)
        # print(image)
        image_grey = rgb2gray(image_initial)
        image = resize(image_grey, (32,32))
        image_ravel = image.ravel()
        
        list_ravel.append(image_ravel)
        # print(list_ravel)
        list_ravel = np.asarray(list_ravel)
        print(list_ravel.shape)
        # image_ravel = np.array(image_ravel)
        # # r = 'r"'
        # # end = '"'
        # # full_file_path_read = r + path + dog_pic + end
        # # print(full_file_path_read)
        # # image = imread(full_file_path_read)
        # pic_title = dog_pic[:-4]
        # print(pic_title)
        # print(str(image_ravel))
        # print(type(image_ravel_str))
        print("*******************************************************")

#         data = data.append(pd.DataFrame({'dog_ID': dog_pic[:-4], 'flattened_img': list_ravel }, index=[0]), ignore_index=True)


# print(data)    
# print(type(data.iloc[0][1]))
# print(data)
data.to_csv(r'df_dogID_and_flattened_img.csv', index = False)
    
#         # path = glob.glob('data/{}/{}/*.jpg'.format(folder, dog_pic))
#         path = glob.glob('data/{}/{}/*.jpg'.format(folder, dog_pic))

#         label = dog_pic
                    
#         for p in path:                
#             X.append(open_images(p))
#             y.append(label)         
                
# X = np.asarray(X)
# print(X[0])
# y = np.asarray(y)

# # image = imread(r"../data/scraped_dog_adoption_petfinder_img_files/test_img.jpg")
# image = imread(r"../../../data/img/img_dumps/48549549_adoptable.jpg")
# # show_img(image)

# red, yellow =   image.copy(), image.copy()
# red[:,:,(1,2)] = 0
# yellow[:,:,2]=0
# # show_images(images=[red,yellow], titles=['Red Intensity','Yellow Intensity'])

# from skimage.color import rgb2gray
# gray_image = rgb2gray(image)
# # show_images(images=[image,gray_image],titles=["Color","Grayscale"])
# # print("Colored image shape:", image.shape) #3 columm matrix
# # print("Grayscale image shape:", gray_image.shape) #2 column matrix
# # print(image) #3*3 matrices made of ints
# gray_image_ravel = gray_image.ravel()
# # print(gray_image.ravel())
# print(gray_image_ravel)





# dog_pics_directory = os.listdir('../../../data/img/img_dumps')[:5]
# print(dog_pics_directory)

# # for folder in data_folders:
    
# for dog_pic in dog_pics_directory:

#     # path = glob.glob('data/{}/{}/*.jpg'.format(folder, dog_pic))
#     path = glob.glob('data/{}/{}/*.jpg'.format(dog_pics_directory, dog_pic))
#     print(path)













#NOT YET WORKING DUE TO IMPORT ERRORS-->
# from skimage.filter import threshold_otsu
# thresh = threshold_otsu(gray_image)
# binary = gray_image > thresh
# show_images(images=[gray_image,binary_image,binary],titles=["Grayscale","Otsu Binary"])

# from skimage.filter import gaussian_filter
# blurred_image = gaussian_filter(gray_image,sigma=20)
# show_images(images=[gray_image,blurred_image],titles=["Gray Image","20 Sigma Blur"])













# from sklearn.naive_bayes import MultinomialNB
# from sklearn.model_selection import train_test_split
# import glob
# from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_curve
# from sklearn.metrics import f1_score, confusion_matrix, balanced_accuracy_score
# from sklearn.metrics import classification_report, mean_squared_error, r2_score
# import numpy as np
# from image_loader import open_images
# import os
# from sklearn.model_selection import KFold
# import matplotlib.pyplot as plt
# # def rmse(y_true, y_predict):
# #     return np.sqrt(mean_squared_error(y_true, y_predict))
# def get_X_y():
#     X = []
#     y = []   
                   
#     # data_folders = ['Train', 'Test']
#     #function fails when dog_pics_directory calls every folder..requires indexing
#     # dog_pics_directory = os.listdir('data/Train')[:5]

#     dog_pics_directory = os.listdir('../../../data/img/img_dumps')[:5]

    
#     for folder in data_folders:
        
#         for dog_pic in dog_pics_directory:
            
#             # path = glob.glob('data/{}/{}/*.jpg'.format(folder, dog_pic))
#             path = glob.glob('data/{}/{}/*.jpg'.format(folder, dog_pic))

#             label = dog_pic
                        
#             for p in path:                
#                 X.append(open_images(p))
#                 y.append(label)         
                   
#     X = np.asarray(X)
#     print(X[0])
#     y = np.asarray(y)
    
#     return X, y, dog_pics_directory
# # def crossVal(k, threshold=0.50):
# #     kf = KFold(n_splits=k)
# #     train_accuracy = []
# #     test_accuracy = []
# #     X, y, _ = get_X_y()
   
# #     for train, test in kf.split(X):
# #         # Split into train and test
# #         X_train, X_test, y_train, y_test = X[train], X[test], y[train], y[test]
# #         # Fit estimator
# #         model = MultinomialNB()
# #         model.fit(X_train, y_train)
# #         # Measure performance
# #         y_hat_trainprob = model.predict_proba(X_train)[:,1]
# #         y_hat_testprob = model.predict_proba(X_test)[:,1]
# #         y_hat_train = (y_hat_trainprob >= threshold).astype(int)
# #         y_hat_test = (y_hat_testprob >= threshold).astype(int)
# #         # metrics
# #         train_accuracy.append(accuracy_score(y_train, y_hat_train))
# #         test_accuracy.append(accuracy_score(y_test, y_hat_test))
# #     return np.mean(train_accuracy), np.mean(test_accuracy) #np.mean(test_errors), np.mean(train_errors), np.mean(test_r2), np.mean(train_r2)
# # def roc_you_curve():
# #     X, y, _ = get_X_y()
# #     model = MultinomialNB()
    
# #     X_train, X_test, y_train, y_test = train_test_split(X,y)
# #     model.fit(X_train,y_train)
# #     probabilities = model.predict_proba(X_test)[:,1]
# #     fpr, tpr, thresholds = roc_curve(y_test, probabilities)
# #     x = np.linspace(0,1, 100)
# #     _, ax = plt.subplots(1, figsize=(10,6))
# #     ax.plot(fpr, tpr, color='firebrick')
# #     ax.plot(x, x, linestyle='--', color ='black', label='Random Guess')
# #     ax.set_xlabel('False Positive Rate (FPR)', fontsize=16)
# #     ax.set_ylabel('True Positive Rate (TPR)', fontsize=16)
# #     ax.set_title('ROC Curve for Random Forest')
# #     plt.legend()
# #     plt.savefig('../images/roccurve.png',  bbox_inches='tight')
# #     return thresholds[fpr>0.3][0]
# def naive_bayes():
#     X, y, dog_pics_directory = get_X_y()
#     X_train, X_test, y_train, y_test = train_test_split(X, y)    
    
#     model = MultinomialNB()
#     model.fit(X_train, y_train)
#     y_pred = model.predict(X_test)
#     # acc = accuracy_score(y_test, y_pred)
#     recall = recall_score(y_test, y_pred, labels=dog_pics_directory, average=None)
#     prec = precision_score(y_test, y_pred, labels=dog_pics_directory, average=None)
#     # fone = f1_score(y_test, y_pred, labels=dog_pics_directory, average=None)
#     con_matrix = confusion_matrix(y_test, y_pred)
#     # bal_acc_scor = balanced_accuracy_score(y_test, y_pred)
#     # report = classification_report(y_test, y_pred, digits=3)
#     return recall, prec, con_matrix
    
# if __name__ == '__main__':
#     # root_mean = rmse(y_true, y_predict)
#     get_it = get_X_y()
    
#     # cross = crossVal(5)
#     # roc = roc_you_curve()
    
#     # naiveb_model = naive_bayes()
#     # print(naiveb_model)

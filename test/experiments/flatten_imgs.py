#NOT LIKELY TO USE THIS

# #small dataset feature selection
# from skimage.io import imread


# # dog_pics_directory = os.listdir('../../../data/img/img_dumps')[:5]


# # for folder in data_folders:
    
# #     for dog_pic in dog_pics_directory:
        
# #         # path = glob.glob('data/{}/{}/*.jpg'.format(folder, dog_pic))
# #         path = glob.glob('data/{}/{}/*.jpg'.format(folder, dog_pic))

# #         label = dog_pic
                    
# #         for p in path:                
# #             X.append(open_images(p))
# #             y.append(label)         
                
# # X = np.asarray(X)
# # print(X[0])
# # y = np.asarray(y)

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





# # dog_pics_directory = os.listdir('../../../data/img/img_dumps')[:5]
# # print(dog_pics_directory)

# # # for folder in data_folders:
    
# # for dog_pic in dog_pics_directory:

# #     # path = glob.glob('data/{}/{}/*.jpg'.format(folder, dog_pic))
# #     path = glob.glob('data/{}/{}/*.jpg'.format(dog_pics_directory, dog_pic))
# #     print(path)













# #NOT YET WORKING DUE TO IMPORT ERRORS-->
# # from skimage.filter import threshold_otsu
# # thresh = threshold_otsu(gray_image)
# # binary = gray_image > thresh
# # show_images(images=[gray_image,binary_image,binary],titles=["Grayscale","Otsu Binary"])

# # from skimage.filter import gaussian_filter
# # blurred_image = gaussian_filter(gray_image,sigma=20)
# # show_images(images=[gray_image,blurred_image],titles=["Gray Image","20 Sigma Blur"])
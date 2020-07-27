







#small dataset feature selection
from skimage.io import imread
image = imread(r"../data/scraped_dog_adoption_petfinder_img_files/test_img.jpg")
# show_img(image)

red, yellow =   image.copy(), image.copy()
red[:,:,(1,2)] = 0
yellow[:,:,2]=0
# show_images(images=[red,yellow], titles=['Red Intensity','Yellow Intensity'])

from skimage.color import rgb2gray
gray_image = rgb2gray(image)
# show_images(images=[image,gray_image],titles=["Color","Grayscale"])
print("Colored image shape:", image.shape)
print("Grayscale image shape:", gray_image.shape)
print(image)


















#NOT YET WORKING DUE TO IMPORT ERRORS-->
# from skimage.filter import threshold_otsu
# thresh = threshold_otsu(gray_image)
# binary = gray_image > thresh
# show_images(images=[gray_image,binary_image,binary],titles=["Grayscale","Otsu Binary"])

# from skimage.filter import gaussian_filter
# blurred_image = gaussian_filter(gray_image,sigma=20)
# show_images(images=[gray_image,blurred_image],titles=["Gray Image","20 Sigma Blur"])
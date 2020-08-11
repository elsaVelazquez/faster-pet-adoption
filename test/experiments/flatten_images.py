from skimage.io import imread
# image = imread(r"../data/scraped_dog_adoption_petfinder_img_files/test_img.jpg")
image = imread(r"0_100.jpg")

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
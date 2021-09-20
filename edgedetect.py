from helper_functions import *

#-----------------------FILL IN THE FOLDER WHERE YOUR IMAGE EXISTS--------------------------
datafolder = "C:/Users/Edgedetect/images/" #path to image folder in he system
imgpath = datafolder + "sample_image.jpg"  #Image name

# Converting the color image to grayscale 
pixel_values = read_colorimg(imgpath)
numb_rows = len(pixel_values) - 2
numb_colns = len(pixel_values[0]) - 2

# Create a data structure to store updated pixel information
new_pixel_values=[[0 for i in range(numb_colns)]for j in range(numb_rows)]
mask = ((-1,0,1), (-2,0,2), (-1,0,1))
def get_slice_2d_list(p,r,c):
    sliced_2d_list=[m[c-1:c+2] for m in p[r-1:r+2]]
    return sliced_2d_list
def flatten(np):
    flatted_list=[j for i in np for j in i]
    return flatted_list
k=-1
for i in pixel_values:
    k=k+1
l=-1
for j in pixel_values[0]:
    l=l+1
for row in range(1,k):
    for col in range(1,l):
        neighbour_pixels = get_slice_2d_list(pixel_values,row,col)
        flatten_np=flatten(neighbour_pixels)
        flatten_msk=flatten(mask)
        mult_result = list(map(lambda x,y: x*y , flatten_np, flatten_msk))
        ad=0
        for i in range(0,len(mult_result)):
            ad= ad+mult_result[i]
        new_pixel_values[row-1][col-1] = ad

# Verifying the result
verify_result(pixel_values, new_pixel_values, mask)
# To view the original image and the edges of the image
view_images(imgpath, new_pixel_values)

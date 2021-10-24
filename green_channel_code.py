#Author:Deryck Ho   StudentID:101181150

import Cimpl
"""
Returns a image with only the green component and without red and blue component to it.
"""

def green_channel():

    file = Cimpl.choose_file()                              #Let user choose an image
    image = Cimpl.load_image(file)                          #Load the image
    new_image= Cimpl.copy(image)                            #Create a copy of the original image
    
    x = Cimpl.get_width(new_image)                          #Get the width of the image
    y = Cimpl.get_height(new_image)                         #Get the height of the iamge
    
    for i in range(x):
        for j in range(y):
            pixelcolor= Cimpl.get_color(new_image,i,j)      #Get RGB of each pixel of the image
            r,g,b= pixelcolor                               #Store the RGB component seperately
            newcolor=Cimpl.create_color(0,g,0)              #Set the Red and Blue component to 0 inorder to have a green filter
            Cimpl.set_color(new_image,i,j,newcolor)         #Apply the green filter
    
    Cimpl.show(new_image)                                   #Show image
    return new_image

green_channel()



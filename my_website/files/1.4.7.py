'''1_4_7: Image Art'''
import PIL
import matplotlib.pyplot as plt
import os.path
import numpy as np  # "as" lets us use standard abbreviations  
         
# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
chrysler_file = os.path.join(directory, 'chrysler2.jpg')
chrysler_img = PIL.Image.open(chrysler_file)
# Read the image data into an array
img = plt.imread(chrysler_file)
 
'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
### change image color ###
height = len(img)
width = len(img[0])
for r in range(height):
    for c in range(width):
        if sum(img[r][c])>450: 
            img[r][c]=[31, 61, 12] # R + G + B = Forrest Green 
#Creating new File
fig.savefig('chrysler3.jpg')
chrysler_file2 = os.path.join(directory, 'chrysler3.jpg')
chrysler_img2 = PIL.Image.open(chrysler_file2) 
# Read the image data into an array
img = plt.imread(chrysler_file2)
                                                      
# resize star
star_file = os.path.join(directory, 'star.png')
star_img = PIL.Image.open(star_file)
star_small = star_img.resize((100, 100)) #star width and height measured in plt
                
# Paste star into Chrysler and display
# Uses alpha from mask
chrysler_img2.paste(star_small, (363, 60), mask=star_small) 
# Display
fig1, ax1 = plt.subplots(1, 2)            
ax1[0].imshow(chrysler_img, interpolation='none')
ax1[1].imshow(chrysler_img2, interpolation='none')
fig1.show() 

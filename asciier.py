# import the opencv library 
import cv2 
from PIL import Image
import numpy as np
import os

ASCII_CHARS = [ '#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']
def resize_image(image, new_width=80):
   (input__width, input__height) = image.size
   aspect_ratio = input__height/float(input__width)
   changed_height = int(aspect_ratio * new_width)
   changed_image = image.resize((new_width, changed_height))
   return changed_image

def make_grey(image):
   return image.convert('L')

def pixel_to_ascii(image, range_width=80):
   pixels_in_image = list(image.getdata())
   pixels_to_chars = [ASCII_CHARS[pixel_value//range_width] for pixel_value in
   pixels_in_image]
   return "".join(pixels_to_chars)

def image_to_ascii(image, new_width=80):
   image = resize_image(image)
   image = make_grey(image)
   pixels_to_chars = pixel_to_ascii(image)
   len_pixels_to_chars = len(pixels_to_chars)
   image_ascii = [pixels_to_chars[index: index + new_width] for index in
   range(0, len_pixels_to_chars, new_width)]
   return "\n".join(image_ascii)
  
  
# define a video capture object 
vid = cv2.VideoCapture(0) 
success , image = vid.read()
  
while success : 
      
    success , image = vid.read()
    cv2.imshow('frame', image) 
    image = Image.fromarray(image,'RGB')
    #print(image)
    print(image_to_ascii(image))
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 
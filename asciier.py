import cv2 
from PIL import Image
import numpy as np

ASCII_CHARS = [ '#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']

def resize_image(img, new_width=80):
   (input__width, input__height) = img.size
   aspect_ratio = input__height/float(input__width)
   changed_height = int(aspect_ratio * new_width)
   changed_img = img.resize((new_width, changed_height))
   return changed_img

def convert_grey(img):
   return img.convert('L')

def pixel_to_ascii(img, range_width=80):
   pixels_in_image = list(img.getdata())
   pixels_to_chars = [ASCII_CHARS[pixel_value//range_width] for pixel_value in pixels_in_image]
   return "".join(pixels_to_chars)

def image_to_ascii(image, new_width=80):
   img = resize_image(image)
   image = convert_grey(img)
   pixels_to_chars = pixel_to_ascii(img)
   image_ascii = [pixels_to_chars[index: index + new_width] for index in range(len(pixels_to_chars), new_width)]
   return "\n".join(image_ascii)
  
vid = cv2.VideoCapture(0) 
success , image = vid.read()
  
while success : 
      
    success , image = vid.read()
    cv2.imshow('frame', image)  #comment here if you don't want to show your webcam
    image = Image.fromarray(image,'RGB')
    #print(image)
    print(image_to_ascii(image))
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
vid.release() 
cv2.destroyAllWindows() 
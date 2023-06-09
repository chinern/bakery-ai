#mathematical model for circumference of bread check
#cluttersort uncheck
#mathematical model for circumference of trapezium
#integration model for cheese
#list to image 
#images of bread

import opencv as cv
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import PIL.ImageOps    

image = Image.open('your_image.png')

inverted_image = PIL.ImageOps.invert(image)

inverted_image.save('new_name.png')

fname = 'image.png'
image = Image.open(fname).convert("L")
arr = np.asarray(image)
plt.imshow(arr, cmap='gray', vmin=0, vmax=255)
plt.show()


#area of a circle equals to three hexagon - leibzeg theory
#test
#x = pi*r*r
#y = pi2*r2*r2
#donut = y - x 


hexagon_area = (3*sqrt(3)*s^2)/2
hexagon_circumference = (1/2)*6*s
circle_half_circumference = (1/2)*3.14159265359*r*r
bottom_diameter = (1/2)*6*s

A = 24*s^2*(1/math.tan(((3.14159265359/96))))
A = 24*x^2(1/math.tan(((3.14159265359/96))))


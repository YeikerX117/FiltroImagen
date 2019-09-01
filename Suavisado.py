import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
##import scipy.misc
##pic=Image.open('D:\Ing Sistemas\Ciencia de datos\Imagen\kratosSon.png')
##plt.imshow(pic)
##key = scipy.misc.imread("D:\Ing Sistemas\Ciencia de datos\Imagen\kratosSon.png")
from skimage import io
import scipy.misc

img=io.imread("D:\Ing Sistemas\Ciencia de datos\Imagen\segunda.png")
# imread lee las imagenes con los pixeles codificados como enteros 
# en el rango 0-255. Por eso la convertimos a flotante y en el rango 0-1
print("- Dimensiones de la imagen:")
print(image.shape)
plt.imshow(image,vmin=0,vmax=1)
key = scipy.misc.imread("D:\Ing Sistemas\Ciencia de datos\Imagen\segunda.png")

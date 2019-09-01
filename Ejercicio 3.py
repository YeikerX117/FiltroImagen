import cv2
import numpy as np
#Arreglos de las imagenes numpy array 
def filtro(imagen, c):
    #Mismas dimensiones que recibe de una imagen 
    #Longitud columnas filas 
    imagen=np.zeros((img.shape[0], img.shape[1]),dtype=np.int)
    for i in range (1, img.shape[0]-1):
        for j in range(1, img.shape[1]-1):
            valor=img.item(i-1,j-1)*c[0][0]+img.item(i-1,j)*c[0][1]
            if valor>255:
                valor=255
            elif valor<0:
                valor=0
            imagen.itemset((i,j), valor)
    return imagen
img=cv2.imread("D:\Ing Sistemas\Ciencia de datos\Imagen\segunda.jpg",0)
matriz=[[1,1,1],[0,0,0],[-1,-1,-1]]
prueba=filtro(img,matriz)
cv2.imwerte("prueba55.jpg", prueba)
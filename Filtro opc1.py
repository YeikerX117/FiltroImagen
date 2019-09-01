import cv2
import numpy as np
#Arreglos de las imagenes numpy array 
def filtro(imagen, c):
    #Mismas dimensiones que recibe de una imagen 
    #Longitud columnas filas 
    imagen=np.zeros((img.shape[0], img.shape[1]),dtype=np.int)
    for i in range (1, img.shape[0]-1):
        for j in range(1, img.shape[1]-1):
            if c<=0:
                #valor=img.item(i+1,j+1)*c-img.item(i+1,j)*c+img.item(i+1,j+1)*c
                valor=img.item(i+1,j+1)*c-img.item(i,j)*c
            elif c>0:
                #valor=img.item(i-1,j-1)*c-img.item(i-1,j)*c-img.item(i+1,j+1)*c
                valor=img.item(i-1,j-1)*c-img.item(i,j)*c
            if valor>255:
                valor=255
            elif valor<0:
                valor=0
            imagen.itemset((i,j), valor)
    return imagen
img=cv2.imread("E:\INGENIERIA DE SISTEMAS\Ciencia de datos\Ejercicio Filtro\Imagenes\Prueba.png",0)
matriz=[[5,1,2],[1,150,1],[0,-100,0]]
mascara=np.sum(matriz)/float(9)
prueba=filtro(img, mascara)
cv2.imwrite("E:\INGENIERIA DE SISTEMAS\Ciencia de datos\Ejercicio Filtro\Imagenes\Prueba2.png", prueba)
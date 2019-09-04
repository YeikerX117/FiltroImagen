#Filtro laplaciano a imagen no ciclica
import cv2
import numpy as np
#Arreglos de las imagenes numpy array 
def filtro(imagen, c, s):
    #Mismas dimensiones que recibe de una imagen 
    #Longitud columnas filas 
    imagen=np.zeros((img.shape[0], img.shape[1]),dtype=np.int)
    for i in range (1, img.shape[0]-1):
        for j in range(1, img.shape[1]-1):
            #if s<=0:
                #valor=img.item(i+1,j+1)*c-img.item(i+1,j)*c+img.item(i+1,j+1)*c
            valor=img.item(i-1,j-1)*c[0][0]+img.item(i-1,j)*c[0][1]+img.item(i-1,j+1)*c[0][2]+img.item(i,j-1)*c[1][0]+img.item(i,j)*c[1][1]+img.item(i,j+1)*c[1][2]+img.item(i+1,j-1)*c[2][0]+img.item(i+1,j)*c[2][1]+img.item(i+1,j+1)*c[2][2]
            valorFinal=valor/float(9)
            #elif c>0:
                #corregir la opreacion
                #valor=img.item(i-1,j-1)*c-img.item(i-1,j)*c-img.item(i+1,j+1)*c
            #    valor=img.item(i-1,j-1)*c-img.item(i,j)*c
            if valorFinal>255:
                valorFinal=255
            elif valorFinal<0:
                valorFinal=0
            imagen.itemset((i,j), valorFinal)
    return imagen
img=cv2.imread("E:\INGENIERIA DE SISTEMAS\Ciencia de datos\Ejercicio Filtro\Imagenes\pp.png",0)
#Colocar for anidado para recibir matrices
mascara=np.zeros((3,3))
for i in range(3):
    for j in range(3):
        mascara[i,j]=int(input("Ingrese el dato ["+str(i)+","+str(j)+"] de la matriz: "))
suma=mascara.sum()
prueba=filtro(img, mascara, suma)
cv2.imwrite("E:\INGENIERIA DE SISTEMAS\Ciencia de datos\Ejercicio Filtro\Imagenes\pp1.png", prueba)

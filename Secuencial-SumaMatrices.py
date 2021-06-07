# Nombres: Juan Barrera & Katherine Barrera
# Universidad Politenica Salesina
#!/usr/bin/env python
# coding: utf-8

    

#Importacion de librerias
import numpy as np


#Funcion para creacion de matriz recibiendo como parametros la fila y la columna y una semilla parala generacion de numeros randoms
def creacionMatrizRandom(fila, columna,semilla):
    #Creacion de semilla para numeros randoms
    np.random.seed(semilla)
    #la funcion nos retorna una matriz randomica con numeros del 0 al 10 y del tamano especificado
    return  np.random.randint(0,10,(fila,columna))

#Funcion para la suma de matrices, pasando la fila y comlumna 
def sumaMatrices(filas, columnas, semilla):
    #Se imprime el tamano del resultado de sumar las dos matrices 
    print("Tamanio de la Matriz ",semilla," Resultante: ",(creacionMatrizRandom(filas,columnas,semilla) + creacionMatrizRandom(filas,columnas,semilla*10)).shape)
    
#Funcion para determinar los divisores de un numero
def divisores(data):
    #Divison de la data en 16 
    numero = data/16
    divisor = 2
    contador = 0
    divisores = []
    valor = 0
    while(numero!=1):
        
        if((numero % divisor) == 0):
            numero = numero / divisor
            contador = contador+1
            valor = divisor**contador
            #print("COntador : ", contador, " divisor: ", divisor, " valor ", valor)
            if(numero == 1):
                divisores.append(valor)
        else:
            if (contador > 0):
                divisores.append(valor)
                contador = 0
            else:
                divisor = divisor+1
    
    return divisores
    

#Funcion principal del programa
if __name__ == "__main__":
    
    #print("\n***********************SECUENCIAL***************************")
    valores = divisores(1000000000)

    #llamada al metodo para realizar la suma de matrices 
    #Se trabaja con 16 sub matrices 
    #cada submatriz tiene un size de 32*1953125
    #dividiendo de esta manera se logra obtener una matriz total de un billo de datos
    sumaMatrices(valores[0],valores[1],1)
    sumaMatrices(valores[0],valores[1],2)
    sumaMatrices(valores[0],valores[1],3)
    sumaMatrices(valores[0],valores[1],4)
    sumaMatrices(valores[0],valores[1],5)
    sumaMatrices(valores[0],valores[1],6)
    sumaMatrices(valores[0],valores[1],7)
    sumaMatrices(valores[0],valores[1],8)
    sumaMatrices(valores[0],valores[1],9)
    sumaMatrices(valores[0],valores[1],10)
    sumaMatrices(valores[0],valores[1],11)
    sumaMatrices(valores[0],valores[1],12)
    sumaMatrices(valores[0],valores[1],13)
    sumaMatrices(valores[0],valores[1],14)
    sumaMatrices(valores[0],valores[1],15)
    sumaMatrices(valores[0],valores[1],16)
    #print("**********************FIN********7 200 000 000******************")

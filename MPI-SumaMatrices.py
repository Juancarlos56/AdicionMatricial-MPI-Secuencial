# Nombres: Juan Barrera & Katherine Barrera
# Universidad Politenica Salesina
#!/usr/bin/env python
# coding: utf-8

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
    
#Importacion de librerias
#from do_something import do_it_now
import numpy as np
from mpi4py import MPI

#Funcion principal del programa
if __name__ == "__main__":
    
    #print("\n***********************MPI***************************")
    
    #Se trabaja con 16 sub matrices 
    #cada submatriz tiene un size de 32*1953125
    #dividiendo de esta manera se logra obtener una matriz total de un billo de datos
    
    #Inicio de MPI con la creacion de rangos
    #Setrabaja con 16 procesadores 
    comm=MPI.COMM_WORLD
    rank = comm.rank

    #si el procesador tiene como identificador 0, ingresa dentro del if
    if rank==0:
        #Obtener los divisores de un billon
        valores = divisores(1000000000)
        #llamada al metodo para realizar la suma de matrices 
        sumaMatrices(valores[0],valores[1],16)
        
        for i in range(1,16):
            #ENvio de divisores 
            comm.send(valores,dest=i)
    
    if rank==1:
        #recibimiento de valores divisores de un billon
        valores=comm.recv(source=0)
        #llamar a la funcion sumar matrices
        sumaMatrices(valores[0],valores[1],1)
    if rank==2:
        valores=comm.recv(source=0)
        sumaMatrices(valores[0],valores[1],2)
    if rank==3:
        valores=comm.recv(source=0)
        sumaMatrices(valores[0],valores[1],3)
    if rank==4:
        valores=comm.recv(source=0)
        sumaMatrices(valores[0],valores[1],4)
    if rank==5:
        valores=comm.recv(source=0)
        sumaMatrices(valores[0],valores[1],5)
    if rank==6: 
        valores=comm.recv(source=0)
        sumaMatrices(valores[0],valores[1],6)
    if rank==7:
        valores=comm.recv(source=0)
        sumaMatrices(valores[0],valores[1],7)
    if rank==8:
        valores=comm.recv(source=0)
        sumaMatrices(valores[0],valores[1],8)
    if rank==9:
        valores=comm.recv(source=0)
        sumaMatrices(valores[0],valores[1],9)
    if rank==10:
        valores=comm.recv(source=0)
        sumaMatrices(valores[0],valores[1],10)
    if rank==11:
        valores=comm.recv(source=0)
        sumaMatrices(valores[0],valores[1],11)
    if rank==12:
        valores=comm.recv(source=0)
        sumaMatrices(valores[0],valores[1],12)
    if rank==13:
        valores=comm.recv(source=0)
        sumaMatrices(valores[0],valores[1],13)
    if rank==14:
        valores=comm.recv(source=0)
        sumaMatrices(valores[0],valores[1],14)
    if rank==15:
        valores=comm.recv(source=0)
        sumaMatrices(valores[0],valores[1],15)
    
    #print("**********************FIN**************************")

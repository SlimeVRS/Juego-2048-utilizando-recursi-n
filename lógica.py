#Matriz
#Matriz 0:      [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#Matriz ej:     [[0,2,4,4],[0,2,2,2],[8,4,0,4],[0,4,4,2]]
#Matriz ej2:    [[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]]
#CAMBIAR LOS RETURNS A LA CREACIÓN DE NÚMEROS Y DE LAS SERIES

import random
import time
import threading
global user

def game_begin():
    global user
    print("¡¡¡BIENVENIDO A 2048!!!")
    time.sleep(1)
    
    user=input("Ingresa tu nombre de usuario: ")
    
    
    time.sleep(1)
    
    Mode=int(input("Sistéma numérico: (0)binario, (1)octal, (2)hexadecimal o (3)decimal: "))
    
    time.sleep(2)
    print('\n',"¡¡¡¡¡INSTRUCCIONES!!!!!",'\n')
    time.sleep(1)
    print("Te mueves con W,A,S,D y solo tienes 5 minutos para completar el juego")
    time.sleep(5)
    print("Prepárate!!!")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("YA!!!",'\n','\n')
    return matriz(Mode)

#Genera la matriz con 16 0 y manda a la evaluación
def matriz(Mode):
    matriz=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    score=0
    return game_start(matriz,score,Mode)

def game_start(matriz,score,Mode):
    fila1=random.randint(0,3)
    columna1=random.randint(0,3)
    fila2=random.randint(0,3)
    columna2=random.randint(0,3)
    num=random.randint(1,5)
    num2=random.randint(1,5)
    if((fila1,columna1)==(fila2,columna2)):
        return game_start(matriz,score,Mode)
    else:
        if(num==1):
            matriz[fila1][columna1]=matriz[fila1][columna1]+4
        else:
            matriz[fila1][columna1]=matriz[fila1][columna1]+2
        if(num2==1):
            matriz[fila2][columna2]=matriz[fila2][columna2]+4
        else:
           matriz[fila2][columna2]=matriz[fila2][columna2]+2
        
        return recorrer_Aux(matriz,score,Mode)

def binario(num):
    if (num==0):
        return ""
    else:
        return binario(num//2) + str(num % 2)

def octal(num):
    if (num==0):
        return ""
    else:
        return octal(num//8) + str(num % 8)

def hexadecimal(num):
    if(num==0):
        return "0"
    if(num<10):
        return num
    if(num==10):
        return "A"
    if(num==11):
        return "B"
    if(num==12):
        return "C"
    if(num==13):
        return "D"
    if(num==14):
        return "E"
    if(num==15):
        return "F"
    else:
        return str(hexadecimal(num//16))+str(num%16)
    
def Modo(Mode,num):
    if(Mode==0):
        if(num==0):
            return "0"
        else:
            return binario(num)
    if(Mode==1):
        if(num==0):
            return "0"
        else:
            return octal(num)
    if(Mode==2):
        return hexadecimal(num)
    if(Mode==3):
        return num
        
def recorrer_Aux(matriz,score,Mode):
    return recorrer_Aux2(matriz,0,0,"",score,Mode)

def recorrer_Aux2(matriz,fila,columna,result,score,Mode):
    if(columna==len(matriz[0])):
        print(result+"\n")
        return recorrer_Aux2(matriz,fila+1,0,"",score,Mode)
    else:
        if(fila==len(matriz)):
            return dirección(matriz,result,score,Mode)
        else:
            temp = Modo(Mode,matriz[fila][columna])
            result=result+str(temp)+"\t"
            return recorrer_Aux2(matriz,fila,columna+1,result,score,Mode)

def dirección(matriz,result,score,Mode):  
    print (result,'\n',"score =",score,'\n')
    a=input("Dame una dirección: arriba(W), derecha(D), abajo(S), izquierda(A): ")
    #for i in range(0,len(matriz)):
        #for j in range(0, len(matriz[i])):
            #print(matriz[i][j])
    if(a=="w"):
        return fill_up(matriz,0,0,0,0,score,Mode)
    if(a=="d"):
        return fill_right(matriz,0,0,0,3,score,Mode)
    if(a=="s"):
        return fill_down(matriz,0,0,3,0,score,Mode)
    if(a=="a"):
        return fill_left(matriz,0,0,0,0,score,Mode)
    else:
        if(a==''):
            print("Dirección no válida")
            return recorrer_Aux(matriz,score,Mode)
        else:
            print("Dirección no válida")
            return recorrer_Aux(matriz,score,Mode)
    
def fill_up(matriz,sumas,ceros,i,j,score,Mode):
    if(i==3 and j==3):
        if(matriz[i][j]!=0):
            if(ceros==0):
                return up(matriz,sumas,0,0,score,Mode)
            else:
                valor_casilla=matriz[i][j]
                matriz[i-ceros][j]=matriz[i-ceros][j]+valor_casilla
                matriz[i][j]=matriz[i][j]*0
                return up(matriz,sumas,0,j,score,Mode)
        else:
            return up(matriz,sumas,0,j,score,Mode)
    if(i==3):
        if(matriz[i][j]!=0):
            if(ceros==0):
                return up(matriz,sumas,0,j,score,Mode)
            else:
                valor_casilla=matriz[i][j]
                matriz[i-ceros][j]=matriz[i-ceros][j]+valor_casilla
                matriz[i][j]=matriz[i][j]*0
                return up(matriz,sumas,0,j,score,Mode)
        else:
            return up(matriz,sumas,0,j,score,Mode)
    
    if(matriz[i][j]==0):
        ceros=ceros+1
        return fill_up(matriz,sumas,ceros,i+1,j,score,Mode)
    
    if(matriz[i][j]!=0):
        if(ceros==0):
            return fill_up(matriz,sumas,ceros,i+1,j,score,Mode)
        else:
            valor_casilla=matriz[i][j]
            matriz[i-ceros][j]=matriz[i-ceros][j]+valor_casilla
            matriz[i][j]=matriz[i][j]*0
            return fill_up(matriz,sumas,0,0,j,score,Mode)
    
def up(matriz,sumas,i,j,score,Mode):
    if(sumas==2):
        if(j==3):
            return generador2(matriz,score,Mode)
        else:
            return fill_up(matriz,0,0,0,j+1,score,Mode)
        
    if(i==3):
        if(j==3):
            return  generador2(matriz,score,Mode)
        else:
            return fill_up(matriz,0,0,0,j+1,score,Mode)
        
    if(matriz[i][j]==matriz[i+1][j]):
        if(matriz[i][j]==0 and matriz[i+1][j]==0):
            return up(matriz,sumas,i+1,j,score,Mode)
        else:
            matriz[i][j]=matriz[i][j]*2
            sumas+=1
            score=score+matriz[i][j]
            matriz[i+1][j]=matriz[i+1][j]*0
            return fill_up(matriz,sumas,0,0,j,score,Mode)

    else:
        return up(matriz,sumas,i+1,j,score,Mode)

def fill_right(matriz,sumas,ceros,i,j,score,Mode):
    if(i==3 and j==0):
        if(matriz[i][j]!=0):
            if(ceros==0):
                return right(matriz,sumas,0,3,score,Mode)
            else:
                valor_casilla=matriz[i][j]
                matriz[i][j+ceros]=matriz[i][j+ceros]+valor_casilla
                matriz[i][j]=matriz[i][j]*0
                return right(matriz,sumas,i,3,score,Mode)
        else:
            return right(matriz,sumas,i,3,score,Mode)
    if(j==0):
        if(matriz[i][j]!=0):
            if(ceros==0):
                return right(matriz,sumas,i,3,score,Mode)
            else:
                valor_casilla=matriz[i][j]
                matriz[i][j+ceros]=matriz[i][j+ceros]+matriz[i][j]
                matriz[i][j]=matriz[i][j]*0
                return right(matriz,sumas,i,3,score,Mode)
        else:
            return right(matriz,sumas,i,3,score,Mode)
    
    if(matriz[i][j]==0):
        ceros=ceros+1
        return fill_right(matriz,sumas,ceros,i,j-1,score,Mode)
    
    if(matriz[i][j]!=0):
        if(ceros==0):
            return fill_right(matriz,sumas,ceros,i,j-1,score,Mode)
        else:
            valor_casilla=matriz[i][j]
            matriz[i][j+ceros]=matriz[i][j+ceros]+valor_casilla
            matriz[i][j]=matriz[i][j]*0
            return fill_right(matriz,sumas,0,i,3,score,Mode)

def right(matriz,sumas,i,j,score,Mode):
    if(sumas==2):
        if(i==3):
            return generador2(matriz,score,Mode)
        else:
            return fill_right(matriz,0,0,i+1,3,score,Mode)
    if(j==0):
        if(i==3):
            return generador2(matriz,score,Mode)
        else:
            return fill_right(matriz,0,0,i+1,3,score,Mode)
        
    if(matriz[i][j]==matriz[i][j-1]):
        if(matriz[i][j]==0 and matriz[i][j-1]==0):
            return right(matriz,sumas,i,j-1,score,Mode)
        else:
            matriz[i][j]=matriz[i][j]*2
            sumas+=1
            score=score+matriz[i][j]
            matriz[i][j-1]=matriz[i][j-1]*0
            return fill_right(matriz,sumas,0,i,3,score,Mode)
    
    else:
        return right(matriz,sumas,i,j-1,score,Mode)

def fill_down(matriz,sumas,ceros,i,j,score,Mode):
    if(i==0 and j==3):
        if(matriz[i][j]!=0):
            if(ceros==0):
                return down(matriz,sumas,3,0,score,Mode)
            else:
                valor_casilla=matriz[i][j]
                matriz[i+ceros][j]=matriz[i+ceros][j]+valor_casilla
                matriz[i][j]=matriz[i][j]*0
                return down(matriz,sumas,3,j,score)
        else:
            return down(matriz,sumas,3,j,score,Mode)
    if(i==0):
        if(matriz[i][j]!=0):
            if(ceros==0):
                return down(matriz,sumas,3,j,score,Mode)
            else:
                valor_casilla=matriz[i][j]
                matriz[i+ceros][j]=matriz[i+ceros][j]+valor_casilla
                matriz[i][j]=matriz[i][j]*0
                return down(matriz,sumas,3,j,score,Mode)
        else:
            return down(matriz,sumas,3,j,score,Node)
    
    if(matriz[i][j]==0):
        ceros=ceros+1
        return fill_down(matriz,sumas,ceros,i-1,j,score,Mode)
    
    if(matriz[i][j]!=0):
        if(ceros==0):
            return fill_down(matriz,sumas,ceros,i-1,j,score,Mode)
        else:
            valor_casilla=matriz[i][j]
            matriz[i+ceros][j]=matriz[i+ceros][j]+valor_casilla
            matriz[i][j]=matriz[i][j]*0
            return fill_down(matriz,sumas,0,3,j,score,Mode)

def down(matriz,sumas,i,j,score,Mode):
    if(sumas==2):
        if(j==3):
            return generador2(matriz,score,Mode)
        else:
            return fill_down(matriz,0,0,3,j+1,score,Mode)
    if(i==0):
        if(j==3):
            return generador2(matriz,score,Mode)
        else:
            return fill_down(matriz,0,0,3,j+1,score,Mode)
        
    if(matriz[i][j]==matriz[i-1][j]):
        if(matriz[i][j]==0 and matriz[i-1][j]==0):
            return down(matriz,sumas,i-1,j,score,Mode)
        else:
            matriz[i][j]=matriz[i][j]*2
            sumas+=1
            score=score+matriz[i][j]
            matriz[i-1][j]=matriz[i-1][j]*0
            return fill_down(matriz,sumas,0,3,j,score,Mode)

    else:
        return down(matriz,sumas,i-1,j,score,Mode)

def fill_left(matriz,sumas,ceros,i,j,score,Mode):
    if(i==3 and j==3):
        if(matriz[i][j]!=0):
            if(ceros==0):
                return left(matriz,sumas,0,0,score,Mode)
            else:
                valor_casilla=matriz[i][j]
                matriz[i][j-ceros]=matriz[i][j-ceros]+matriz[i][j]
                matriz[i][j]=matriz[i][j]*0
                return left(matriz,sumas,i,0,score,Mode)
        else:
            return left(matriz,sumas,i,0,score,Mode)
    if(j==3):
        if(matriz[i][j]!=0):
            if(ceros==0):
                return left(matriz,sumas,i,0,score,Mode)
            else:
                valor_casilla=matriz[i][j]
                matriz[i][j-ceros]=matriz[i][j-ceros]+matriz[i][j]
                matriz[i][j]=matriz[i][j]*0
                return left(matriz,sumas,i,0,score,Mode)
        else:
            return left(matriz,sumas,i,0,score,Mode)
    
    if(matriz[i][j]==0):
        ceros=ceros+1
        return fill_left(matriz,sumas,ceros,i,j+1,score,Mode)
    
    if(matriz[i][j]!=0):
        if(ceros==0):
            return fill_left(matriz,sumas,ceros,i,j+1,score,Mode)
        else:
            valor_casilla=matriz[i][j]
            matriz[i][j-ceros]=matriz[i][j-ceros]+valor_casilla
            matriz[i][j]=matriz[i][j]*0
            return fill_left(matriz,sumas,0,i,0,score,Mode)

def left(matriz,sumas,i,j,score,Mode):
    if(sumas==2):
        if(i==3):
            return generador2(matriz,score,Mode)
        else:
            return fill_left(matriz,0,0,i+1,0,score,Mode)
    if(j==3):
        if(i==3):
            return generador2(matriz,score,Mode)
        else:
            return fill_left(matriz,0,0,i+1,0,score,Mode)
        
    if(matriz[i][j]==matriz[i][j+1]):
        if(matriz[i][j]==0 and matriz[i][j+1]==0):
            return left(matriz,sumas,i,j+1,score,Mode)
        else:
            matriz[i][j]=matriz[i][j]*2
            sumas+=1
            score=score+matriz[i][j]
            matriz[i][j+1]=matriz[i][j+1]*0
            return fill_left(matriz,sumas,0,i,0,score,Mode)
    else:
        return left(matriz,sumas,i,j+1,score,Mode)

def generador2(matriz,score,Mode):
    fila1=random.randint(0,3)
    columna1=random.randint(0,3)
    num=random.randint(1,5)
    if(matriz[fila1][columna1]!=0):
        return generador2(matriz,score,Mode)
    else:
        if(num==1):
            matriz[fila1][columna1]=matriz[fila1][columna1]+4
            return WIN(matriz,0,0,score,Mode)
        else:
            matriz[fila1][columna1]=matriz[fila1][columna1]+2
            return WIN(matriz,0,0,score,Mode)

def WIN(matriz,i,j,score,Mode):
    global user
    if(i==3 and j==3):
        if(matriz[i][j]==2048):
            return print("GANASTE", user, "\t Puntaje =",score)
        else:
            GAME_OVER(matriz,0,0,0,score,Mode)
    if(i==3):
        if(matriz[i][j]==2048):
            return print("GANASTE", user, "\t Puntaje =",score)
        else:
            WIN(matriz,0,j+1,score,Mode)
    if(matriz[i][j]==2048):
        return print("GANASTE", user, "\t Puntaje =",score)
    else:
        return WIN(matriz,i+1,j,score,Mode)

def GAME_OVER(matriz,ceros,i,j,score,Mode):
    if(i==3 and j==3):
        if(matriz[i][j]==0):
            return recorrer_Aux(matriz,score,Mode)
        else:
            if(ceros==0):
                return GAME_OVERH(matriz,0,0,score,Mode)
            else:
                return recorrer_Aux(matriz,score,Mode)

    if(j==3):
        if(matriz[i][j]==0):
            ceros=ceros+1
            return GAME_OVER(matriz,ceros,i+1,0,score,Mode)
        else:
            return GAME_OVER(matriz,ceros,i+1,0,score,Mode)
    
    if(matriz[i][j]==0):
        ceros=ceros+1
        return recorrer_Aux(matriz,score,Mode)
    else:
        return GAME_OVER(matriz,ceros,i,j+1,score,Mode)

def GAME_OVERH(matriz,i,j,score,Mode):
    if(j==3 and i==3):
        return GAME_OVERV(matriz,0,0,score,Mode)    
    if(j==3):
        return GAME_OVERH(matriz,i+1,0,score,Mode)
    if(matriz[i][j]==matriz[i][j+1]):
        return recorrer_Aux(matriz,score,Mode)
    else:
        return GAME_OVERH(matriz,i,j+1,score,Mode)

def GAME_OVERV(matriz,i,j,score,Mode):
    global user
    if(j==3 and i==3):
        return print("GAME OVER \t Puntaje =",score)    
    if(i==3):
        return GAME_OVERV(matriz,0,j+1,score,Mode)
    if(matriz[i][j]==matriz[i+1][j]):
        return recorrer_Aux(matriz,score,Mode)
    else:
        return GAME_OVERV(matriz,i+1,j,score,Mode)

def countdown(t):
    if(t>0):
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
        return countdown(t)
    else:
        return print ("GAME OVER!!!")
game_begin()

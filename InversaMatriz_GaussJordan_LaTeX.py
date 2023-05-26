#Author: Angel Manuel Gonzalez Lopez

# v1.1
# Metodo de Gauss-Jordan
# dada una matriz invertible que no tenga ningun 0 en su diagonal principal
# calcula su inversa usando el metodo de gauss jordan
#n formato LaTeX

import numpy as np
from fractions import Fraction
from decimal import Decimal


# # # # # # # # # IMPRIMIR MODO LATEX  # # # # # # # # # 
def ImprimirPosibleFraccion(esFraccion):
    if esFraccion.denominator == 1:
        print(esFraccion, end='')
    else:
        if esFraccion.numerator<0:
            print("-\\frac{%d}{%d}" % (-esFraccion.numerator, esFraccion.denominator) , end='')
        else:
            print("\\frac{%d}{%d}" % (esFraccion.numerator, esFraccion.denominator) , end='')


def ImprimirMatriz(matrix):
    print("\\begin{pmatrix}")
    for fila in matrix:
        print("\t", end='')
        for esFraccion in fila:
            ImprimirPosibleFraccion(esFraccion)
            print(" & ", end='')
        print("\b\b\b  \\\\ ")
    print("\\end{pmatrix}")

def ImprimirMatrizAumentada(matrix):
    mitadColumnas = len(matrix[0]) // 2
    print("\\begin{pmatrix}")
    for fila in matrix:
        print("\t", end='')
        #primera parte
        for esFraccion in fila[:mitadColumnas]:
            ImprimirPosibleFraccion(esFraccion)
            print(" & ", end='')
        #mitad
        print(" \\vline & ", end='')
        #segunda parte
        for esFraccion in fila[mitadColumnas:]:
            ImprimirPosibleFraccion(esFraccion)
            print(" & ", end='')
        print("\b\b\b  \\\\ ")
    print("\\end{pmatrix}")


# # # # # # # # # OPERACIONES ELEMENTALES  # # # # # # # # # 
# Ri <-> Rj
def IntercambioDosFilas(matrix, i, j):
    temp = np.copy(matrix[i, :])
    matrix[i, :] = matrix[j, :]
    matrix[j, :] = temp

#Cambio de un fila por un multiplo de sı misma
#Ri - > c*R_i
def FilaPorMultiplo(matrix, i, c):
    matrix[i, :] *= c

#Ri -> Ri + c Rj
def SumarFila(matrix, i, j, c):
    matrix[i, :] += c * matrix[j, :]


def PRINTIntercambioDosFilas(i, j):
    print("\\\\ & \\xleftrightarrow{R_%d\\to " % (i+1)  , end='')
    print("R_%d}"% (j+1))


def PRINTFilaPorMultiplo(i, c):
    print("\\\\ & \\xrightarrow{R_%d\\to " % (i+1)  , end='')
    ImprimirPosibleFraccion(c)
    print("R_%d}"% (i+1))

def PRINTSumarFila(i, j, c):
    print("\\\\ & \\xrightarrow{R_%d\\to R_%d+" % (i+1 , i+1)  , end='')
    ImprimirPosibleFraccion(c)
    print("R_%d}"% (j+1))

# # # # # # # # # ENTRADA DATOS  # # # # # # # # # 

N = int(input())
M = int(input())
matriz = []
for i in range(N):
    fila = input().split()
    fila = [Fraction(e) for e in fila]    
    matriz.append(fila)

print("\n")



# # # # # # # # # MATRIZ AUMENTADA  # # # # # # # # # 
#identidad de tamano N
id = []
for i in range(N):
    fila = []
    for j in range(N):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
    id.append(fila)

#aumentada
mA = []
for i in range(N):
    mA.append( matriz[i]+id[i] )

print("\n")

ImprimirMatriz(matriz)

print("\n\n\n")



# # # # # # # # # Gauss Jordan  # # # # # # # # # 
#notar que la matriz era de N| por M_, así mA es de N| por 2M_ 
mA = np.array(mA)
print("\\begin{align*}")
ImprimirMatrizAumentada(mA)
for n in range(N):
    if mA[n][n]!=0:
        #poner primera fila a 1
        if mA[n][n]!=1:
            c= Fraction(1)/mA[n][n]
            FilaPorMultiplo(mA, n, c )
            #imprimir
            PRINTFilaPorMultiplo(n,c)
            ImprimirMatrizAumentada(mA)

        for i in range(N):
            #poner columna i a puros 0
            if i!=n and mA[i][n]!=0:
                c= -mA[i][n]
                SumarFila(mA, i, n, c )
                #impirmir
                PRINTSumarFila(i, n, c )
                ImprimirMatrizAumentada(mA)

    else:
        print("hijoles")

print("\\end{align*}")

# # # # # # # # # Imprimir la inversa  # # # # # # # # # 
#recordatorio, todo esto es suponinedo que gauus Jordan funciona
mitadColumnas = len(mA[0]) // 2
LaMatrizInversa = mA[:,mitadColumnas:]

print("\nAsí")
print("\\begin{equation*}")
print("\tA^{-1}=")
ImprimirMatriz(LaMatrizInversa)
print("\\end{equation*}")
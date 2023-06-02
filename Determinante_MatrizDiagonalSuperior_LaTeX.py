#Author: Angel Manuel Gonzalez Lopez

# v1.3
# Calcular determinante usando matriz diagonal 
# dada una matriz A  
# reducir la matriz A o A|b mediante trasnformaciones del tipo Rj ->Rj+cRk
# en formato LaTeX

# Input:
# En la primera linea un entero N
# En las sigueintes N lineas cotiene N numeros (fracciones o enteros o decimales) separados por un espacio


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

def ImprimirDetMatriz(matrix, N):
    print("\\begin{array}{|", end='')
    for i in range(N):
        print("c", end='')
    print("|}")
    for fila in matrix:
        print("\t", end='')
        for esFraccion in fila:
            ImprimirPosibleFraccion(esFraccion)
            print(" & ", end='')
        print("\b\b\b  \\\\ ")
    print("\\end{array}")

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


def PRINTIntercambioDosFilas(i, j, primera):
    if not primera:
         print("\\\\", end='')
    print(" & \\xleftrightarrow{R_%d\\to " % (i+1)  , end='')
    print("R_%d}"% (j+1))


def PRINTFilaPorMultiplo(i, c, primera):
    if not primera:
         print("\\\\", end='')
    print(" & \\xrightarrow{R_%d\\to " % (i+1)  , end='')
    ImprimirPosibleFraccion(c)
    print("R_%d}"% (i+1))

def PRINTSumarFila(i, j, c, primera):
    if not primera:
         print("\\\\", end='')
    print("& \\xrightarrow{R_%d\\to R_%d+" % (i+1 , i+1)  , end='')
    ImprimirPosibleFraccion(c)
    print("R_%d}"% (j+1))



# # # # # # # # # Gauss Jordan  # # # # # # # # # 
# # # # # # # # # Triangular Superior  # # # # # # # # # 
def MatrizTriangularSuperior(A,N):
    PrimerT= True;
    print("\\begin{align*}")
    ImprimirMatriz(A)
    for n in range(N):
        if A[n][n]!=0:
            for i in range(n,N):
                #poner columna i a puros 0
                if i!=n and A[i][n]!=0:
                    c= -A[i][n]/A[n][n]
                    SumarFila(A, i, n, c )
                    #impirmir
                    PRINTSumarFila(i, n, c, PrimerT )
                    PrimerT=False
                    ImprimirMatriz(A)
        else:
            #hay que agregar que entonces busque otro candidato para poder cancelar el que se quiere
            print("hijoles")
    print("\\end{align*}")


# # # # # # # # # Determinante Triangular Superior  # # # # # # # # # 
def DeterminanteMatrizTriangularSuperior(A,N):
    Det= Fraction(1);
    for n in range(N):
        Det*= A[n][n]
        print("\\Pa{", end='')
        ImprimirPosibleFraccion(A[n][n])
        print("}", end='')
    return Det;


# # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # ENTRADA DATOS  # # # # # # # # # 
N = int(input())
A = []
for i in range(N):
    fila = input().split()
    fila = [Fraction(e) for e in fila]    
    A.append(fila)

print("\n")
 

# # # # # # # # # MATRIZ A # # # # # # # # # 
A = np.array(A)
A2 = np.array(A)
ImprimirMatriz(A)

print("\n\n\n")

MatrizTriangularSuperior(A2,N)

print("\nAsí")


print("\\begin{equation*}")
ImprimirDetMatriz(A,N)

print("=", end=' ')
ImprimirDetMatriz(A2,N)

print("=", end=' ')
c=DeterminanteMatrizTriangularSuperior(A2,N)

print("=", end=' ')
ImprimirPosibleFraccion(c)

print("\n\\end{equation*}")
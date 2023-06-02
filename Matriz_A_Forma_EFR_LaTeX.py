#Author: Angel Manuel Gonzalez Lopez

# v1.2
# Metodo de Gauss-Jordan
# dada una matriz A  (y dado un vector b)
# reducir la matriz A o A|b mediante trasnformaciones elemnentales a su forma ER y EFR
# en formato LaTeX

# Input:
# En la primera linea un entero N
# en la segunda linea un entero M (que es el mismo N=M)
# en las sigueintes N lineas ontiene M fracciones o enteros o decimales (los vuelve fracciones) separadas por un espacio


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

def ImprimirMatrizAumentada(matrix, n, m):
    print("\\begin{pmatrix}")
    
    for fila in matrix:
        contador=1;
        print("\t", end='')
        #primera parte
        for esFraccion in fila[:m]:
            ImprimirPosibleFraccion(esFraccion)
            print(" & ", end='')
            contador=contador+1
        #mitad
        if len(fila)+1>contador:
            print(" \\vline & ", end='')
        #segunda parte
        for esFraccion in fila[m:]:
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
# # # # # # # # # Diagonal  # # # # # # # # # 
def MatrizDiagonal(A,N,M):
    PrimerT= True;
    print("\\begin{align*}")
    ImprimirMatrizAumentada(A,N,M)
    for n in range(N):
        if A[n][n]!=0:
            #poner primera fila a 1
            if A[n][n]!=1:
                c= Fraction(1)/A[n][n]
                FilaPorMultiplo(A, n, c )
                #imprimir
                PRINTFilaPorMultiplo(n,c, PrimerT )
                PrimerT=False
                ImprimirMatrizAumentada(A,N,M)
            for i in range(N):
                #poner columna i a puros 0
                if i!=n and A[i][n]!=0:
                    c= -A[i][n]
                    SumarFila(A, i, n, c )
                    #impirmir
                    PRINTSumarFila(i, n, c , PrimerT )
                    PrimerT=False
                    ImprimirMatrizAumentada(A,N,M)
        else:
            print("hijoles")
    print("\\end{align*}")

# # # # # # # # # Gauss Jordan  # # # # # # # # # 
# # # # # # # # # Triangular Superior  # # # # # # # # # 
def MatrizTriangularSuperior(A,N,M):
    PrimerT= True;
    print("\\begin{align*}")
    ImprimirMatrizAumentada(A,N,M)
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
                    ImprimirMatrizAumentada(A,N,M)
        else:
            #hay que agregar que entonces busque otro candidato para poder cancelar el que se quiere
            print("hijoles")
    print("\\end{align*}")




# # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # ENTRADA DATOS  # # # # # # # # # 
N = int(input())
M = int(input())
A = []
for i in range(N):
    fila = input().split()
    fila = [Fraction(e) for e in fila]    
    A.append(fila)

SeraQueAumento = int(input())

if SeraQueAumento==1:
    B = input().split()
    B = [Fraction(e) for e in B]     

print("\n")
# # # # # # # # # MATRIZ AUMENTADA  A|b # # # # # # # # #
#notar que la matriz A es de N|  M_, así A_b es de N+1|  M_  
#aumentada
if SeraQueAumento==1:
    A_b = []
    for i in range(N):
        fila = A[i]
        fila.append(B[i])
        A_b.append( fila )

# # # # # # # # # # # # # # DIAGONAL # # # # # # # # # # # # # # #
print("% % % % % % % % % % % % % % % % % % % % % % % % % % % % % %  ")
print("% % % % % % % % % % % % Diagonal % % % % % % % % % % % % %  ")
if SeraQueAumento==1:
    Mat = np.array(A_b)
    ImprimirMatrizAumentada(A,N,M)
else:
    Mat = np.array(A)
    ImprimirMatriz(A)
print("\n\n\n")
MatrizDiagonal(Mat,N,M)


# # # # # # # # # # # # # # # TRIANGULAR # # # # # # # # # # # # # # #
print("\n\n\n\n\n")
print("% % % % % % % % % % % % % % % % % % % % % % % % % % % % % %  ")
print("% % % % % % % % % % Triangular Sup % % % % % % % % % % % % %  ")
if SeraQueAumento==1:
    Mat = np.array(A_b)
    ImprimirMatrizAumentada(A,N,M)
else:
    Mat = np.array(A)
    ImprimirMatriz(A)
print("\n\n\n")
MatrizTriangularSuperior(Mat,N,M)
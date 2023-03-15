import math

#crea un programa modular de un triangulo atravez de valor entrado por teclados
def calcularArea(a,b):
    area = (a*b)/2
    return area

print('Ingresar altura')
a = float(input())
print('Ingresar base')
b = float(input())

print('El area es ' + str(calcularArea(a, b)))

#------------------------------------------------------------
#crea un programa que calcule el area de un circulo
def areaCirculo(r):
    area = math.pi * math.pow(r, 2)
    return area

print('Ingresa el radio del circulo')
r = float(input())

print('El area del circulo es '+str(areaCirculo(r)))


#----------------------------------------
#programa modular que calcule la edad dado el año, el año debe ser ingresado por el usuario
def CalcularEdad(nac, actual):
    edad = actual - nac
    return edad

print('Ingresa el año de nacimiento')
nac = float(input())
print('Ingresa el año de actual')
actual = float(input())

print('La edad es:' + str(CalcularEdad(nac, actual))+'años')

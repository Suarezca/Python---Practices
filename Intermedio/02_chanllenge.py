### RETOS ##

"""Escribir un programa que muestre en pantalla los
números del 1 al 100, sustituyendo los múltiplos de 3
por la palabra “fizz”, los múltiplos de 5 por “buzz” 
y los múltiplos de ambos, es decir, los múltiplos 
de 3 y 5 (o de 15), por la palabra “fizzbuzz”."""

def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)
        
fizz_buzz()



"""Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
 - Un Anagrama consiste en formar una palabra reordenando TODAS
   las letras de otra palabra inicial.
  NO hace falta comprobar que ambas palabras existan.
  Dos palabras exactamente iguales no son anagrama.
"""

def is_anagrama():        
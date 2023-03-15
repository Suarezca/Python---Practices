def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


num = 5
fact = factorial(num)
print("El factorial de", num, "es", fact)



class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        print("Hola, mi nombre es", self.nombre, "y tengo", self.edad, "años.")



persona1 = Persona("Juan", 30)
persona1.saludar()


# "append" es un método en Python que se utiliza para agregar elementos a una lista. El método "append" toma un solo argumento, que puede ser cualquier tipo de datos y lo agrega al final de la lista. Por ejemplo:
lista = [1, 2, 3]
lista.append(4)
print(lista) # output: [1, 2, 3, 4]

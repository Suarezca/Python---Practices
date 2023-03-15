#Abstracción: la clase Animal es una abstracción ya que no se puede instanciar. En cambio, las clases Perro y Gato son implementaciones concretas de la clase Animal.

#Encapsulamiento: la clase Animal y sus métodos están encapsulados dentro del objeto, de manera que las variables de instancia como nombre, edad, salud, vacunado, y peso sólo pueden ser accedidas mediante los métodos definidos en la clase.

#Herencia: la clase Perro y Gato heredan atributos y métodos de la clase Animal con la instrucción super().__init__() en el método __init__(). Por ejemplo, cada vez que creamos una nueva instancia de Perro, también le estamos pasando los valores nombre y edad al constructor de la clase padre. Además, tienen un comportamiento particular para los métodos hablar(), recibir_vacuna() y aumentar_peso().

#Polimorfismo: tanto la clase Perro como Gato comparten el método hablar(), pero tienen una implementación diferente para este. Esto significa que aunque tienen el mismo nombre de método, pueden tener resultados diferentes según su respectiva lógica de negocio.


class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hablar(self):
        pass

class Perro(Animal):
    def __init__(self,nombre,edad,salud,vacunado):
        super().__init__(nombre,edad)
        self.salud=salud
        self.vacunado=vacunado

    def hablar(self):
        return "Guau!"
     
    def recibir_vacuna(self):
        self.vacunado = True

class Gato(Animal):
    def __init__(self,nombre,edad,peso):
        super().__init__(nombre,edad)
        self.peso=peso

    def hablar(self):
        return "Miau!"

    def aumentar_peso(self, peso_extra):
        self.peso += peso_extra
        

# Creamos una instancia de la clase Perro
perro1 = Perro("Fido", 5, "Saludable", False)

# Llamamos al método hablar() de la clase Perro
print(perro1.hablar())   # Salida: Guau!

# Vacunamos al perro y actualizamos su estado en el objeto
perro1.recibir_vacuna()

# Creamos una instancia de la clase Gato
gato1 = Gato("Garfield", 3, 4.5)

# Llamamos al método hablar() de la clase Gato
print(gato1.hablar())    # Salida: Miau!

# Aumentamos el peso del gato y actualizamos su estado en el objeto
gato1.aumentar_peso(0.5)

# Imprimimos los atributos de cada animal
print(perro1.__dict__)
print(gato1.__dict__)

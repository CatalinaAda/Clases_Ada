# Definir una clase en pytgon

# definimos una clase llamada coche

class Coche:
    # Método _init_ es el constructor que se llama al crear un nuevo objeto 
    def __init__(self, marca, modelo):
        #Self es una referencia al objeto que estamos creando
        #inicializamos los atributos de la instacia
        self.marca = marca # Atributo de instancia: guarda la marca del coche 
        self.modelo = modelo  # Atributo de instancia: guarda el modelo del coche 
        
# La clase coche es una plantilla para crear objetos de tipo auto.
# Contiene un método constructor _init_ que inicializa los atributos especificos de cada coche
# como por ejemplo: marca, modelo, usando la referencia self para distinguir entre las propiedades del objeto y los parámetros pasados al construtor

#Definir la clase persona
class Persona:
    def __init__(self, nombre, edad):
        #inicializar las propiedades del objeto
        self.nombre = nombre
        self.edad = edad
        
        
# Crear un objeto de la clase persona

persona1 = Persona("Ana","33")

#acceder a las propiedades del objeto
print(persona1.nombre)
print(persona1.edad)

#LA clase persona define un opbjeto que tiene propiedades como nombre y edad.
#Al instanciar persona1 con valores específicos, se crean atributps únicos que representan el estado de ese objeto
#Se puede acceder a estas propiedades utilizando la notación de punto, lo que permite obtener información 


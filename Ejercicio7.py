class Persona():
    def __init__(self, nombre, edad, dni):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    def __str__(self) -> str:
        return f'{self.__nombre} tiene {self.__edad} años'
    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if nuevo_nombre == str:
            self.__nombre = nuevo_nombre
        else: 
            print("Ingrese un nombre")

    @property
    def edad(self):
        return self.__edad
    @nombre.setter
    def edad(self, nueva_edad):
        if nueva_edad == int:
            self.__edad = nueva_edad
        else: 
            print("Ingrese un numero")
    
    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, nuevo_dni):
        if nuevo_dni == int:
            self.__dni = nuevo_dni
        else: 
            print("Ingrese un numero")



def mostrar(self, Persona):
    return f'Nombre: {self.__nombre} , {self.__edad} años, DNI: {self.__dni}'
    
def es_mayor_de_edad(self, Persona):
    if Persona >= 18:
        print('Es mayor de edad')
    else:
        print('Es menor de edad')


nueva_persona = Persona ('lucas',42,36677488)
print(nueva_persona)
mostrar(nueva_persona)
es_mayor_de_edad(nueva_persona)
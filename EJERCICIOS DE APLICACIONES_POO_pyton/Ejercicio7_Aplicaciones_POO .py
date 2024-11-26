# Una familia quiere digitalizar el árbol genealógico, están dispuestos a contratar un ingeniero que 
# les haga un programa donde ellos puedan almacenar la información: nombres, apellidos, edad, género 
# y generación (bisabuelos, abuelos, padres, yo, hijos). Teniendo en cuenta los parámetros dados por 
# la familia. Usted debe hacer un programa empleando POO en Python. En una clase llamada Persona () 
# se pueden ingresar los datos básicos (nombre, apellido, edad y genero) de los familiares, según 
# criterio de edad él pueda ubicarse en la Clase Generación () correspondiente y cuando desee mostrar 
# en pantalla su árbol genealógico pueda hacerse: ascendente o descendente cronológicamente y aparecer 
# todos los datos de la persona.
class Persona:
    def _init_(self, nombre, apellido, edad, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero

    def _str_(self):
        return f"{self.nombre} {self.apellido}, {self.edad} años, {self.genero}"


class Generacion:
    def _init_(self):
        self.familiares = {
            "Bisabuelos": [],
            "Abuelos": [],
            "Padres": [],
            "Yo": [],
            "Hijos": []
        }

    def agregar_familiar(self, persona):
        if persona.edad >= 85:
            self.familiares["Bisabuelos"].append(persona)
        elif 60 <= persona.edad < 85:
            self.familiares["Abuelos"].append(persona)
        elif 30 <= persona.edad < 60:
            self.familiares["Padres"].append(persona)
        elif 18 <= persona.edad < 30:
            self.familiares["Yo"].append(persona)
        else:
            self.familiares["Hijos"].append(persona)

    def mostrar_arbol(self):
        for generacion, personas in self.familiares.items():
            print(f"\n{generacion}:")
            if personas:
                for persona in personas:
                    print(f"  - {persona}")
            else:
                print("  (Sin familiares en esta generación)")



def main():
    arbol = Generacion()

    while True:
        print("\n1. Agregar familiar")
        print("2. Mostrar árbol genealógico")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            edad = int(input("Ingrese la edad: "))
            genero = input("Ingrese el género (Masculino/Femenino): ")

            familiar = Persona(nombre, apellido, edad, genero)
            arbol.agregar_familiar(familiar)
            print("\nFamiliar agregado exitosamente.")
        elif opcion == "2":
            print("\nÁrbol genealógico:")
            arbol.mostrar_arbol()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


main()
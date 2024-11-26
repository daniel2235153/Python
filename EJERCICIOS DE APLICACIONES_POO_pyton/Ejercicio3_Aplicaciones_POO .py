# Diseñe un programa para un zoológico, por medio de clases y objetos. Su programa debe permitir
#  almacenar información de animales por especies (terrestre, aéreos y acuáticos) y las características
#  de cada uno por especie. Aclaración: Cuando se ejecuta el programa debe preguntar que especie
#  de animal desea ingresar, según su selección haremos una clase para cada especie y el objeto que se
#  cree solicita las características pertinentes. 
class Zoologico:
    def __init__(self):
        self.animales = {"Terrestres": [], "Aéreos": [], "Acuáticos": []}

    def agregar_animal(self):
        print("Seleccione la especie del animal que desea registrar:")
        print("1. Terrestre")
        print("2. Aéreo")
        print("3. Acuático")
        opcion = int(input("Digite una opción: "))
        
        if opcion == 1:
            self.agregar_terrestre()
        elif opcion == 2:
            self.agregar_aereo()
        elif opcion == 3:
            self.agregar_acuatico()
        else:
            print("Opción inválida. Intente nuevamente.")
            self.agregar_animal()

    def agregar_terrestre(self):
        nombre = input("Nombre del animal: ")
        habitat = input("Hábitat (bosque, desierto, etc.): ")
        dieta = input("Dieta (herbívoro, carnívoro, omnívoro): ")
        patas = int(input("Número de patas: "))
        self.animales["Terrestres"].append({"Nombre": nombre, "Hábitat": habitat, "Dieta": dieta, "Patas": patas})
        print("Animal terrestre registrado con éxito.")
        self.menu()

    def agregar_aereo(self):
        nombre = input("Nombre del animal: ")
        habitat = input("Hábitat (selva, montaña, etc.): ")
        dieta = input("Dieta (herbívoro, carnívoro, omnívoro): ")
        envergadura = input("Envergadura alar (en metros): ")
        self.animales["Aéreos"].append({"Nombre": nombre, "Hábitat": habitat, "Dieta": dieta, "Envergadura": envergadura})
        print("Animal aéreo registrado con éxito.")
        self.menu()

    def agregar_acuatico(self):
        nombre = input("Nombre del animal: ")
        habitat = input("Hábitat (mar, río, etc.): ")
        dieta = input("Dieta (herbívoro, carnívoro, omnívoro): ")
        profundidad = input("Profundidad máxima que alcanza (en metros): ")
        self.animales["Acuáticos"].append({"Nombre": nombre, "Hábitat": habitat, "Dieta": dieta, "Profundidad": profundidad})
        print("Animal acuático registrado con éxito.")
        self.menu()

    def listar_animales(self):
        print("\n--- Animales registrados ---")
        for especie, lista in self.animales.items():
            print(f"\n{especie}:")
            for animal in lista:
                print(animal)
        self.menu()

    def buscar_animal(self):
        nombre = input("Digite el nombre del animal que desea buscar: ")
        encontrado = False
        for especie, lista in self.animales.items():
            for animal in lista:
                if animal["Nombre"].lower() == nombre.lower():
                    print(f"Animal encontrado en {especie}: {animal}")
                    encontrado = True
                    break
        if not encontrado:
            print("Animal no encontrado.")
        self.menu()

    def menu(self):
        print("\n--- Menú del Zoológico ---")
        print("1. Agregar animal")
        print("2. Listar animales")
        print("3. Buscar animal")
        print("4. Salir")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            self.agregar_animal()
        elif opcion == 2:
            self.listar_animales()
        elif opcion == 3:
            self.buscar_animal()
        elif opcion == 4:
            print("¡Gracias por usar el programa del zoológico!")
        else:
            print("Opción inválida. Intente nuevamente.")
            self.menu()


zoo = Zoologico()
zoo.menu()

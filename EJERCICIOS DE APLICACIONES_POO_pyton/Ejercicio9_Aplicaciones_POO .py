#Diseñe un algoritmo empleando la programación orientada a objetos 
# con Python para resolver el problema mostrado en la siguiente imagen. 
# Se presenta un diagrama de clases para vehículos con atributos especificados. 
# Cree los métodos necesarios para permitir ingresar vehículos en las diferentes clases y poder mostrar 
# la información contenida en ellos. Adicional cree al menos 2 métodos para cada clase que usted considere
#  importantes y necesarios en la ejecución del mismo. Su programa debe tener menús de acceso y
#  permitir: agregar, editar y borrar información
class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def mostrar_informacion(self):
        return f"Color: {self.color}, Ruedas: {self.ruedas}"


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        return f"{info}, Velocidad: {self.velocidad} km/h, Cilindrada: {self.cilindrada} cc"


class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        return f"{info}, Carga: {self.carga} kg"


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        return f"{info}, Tipo: {self.tipo}"


class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        return f"{info}, Velocidad: {self.velocidad} km/h, Cilindrada: {self.cilindrada} cc"


class GestionVehiculos:
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        print("Vehículo agregado exitosamente.")

    def listar_vehiculos(self):
        if not self.vehiculos:
            print("No hay vehículos registrados.")
        else:
            print("\nListado de vehículos:")
            for i, vehiculo in enumerate(self.vehiculos, 1):
                print(f"{i}. {vehiculo.mostrar_informacion()}")

    def eliminar_vehiculo(self, indice):
        if 0 <= indice < len(self.vehiculos):
            eliminado = self.vehiculos.pop(indice)
            print(f"Vehículo eliminado: {eliminado.mostrar_informacion()}")
        else:
            print("Índice inválido.")

    def editar_vehiculo(self, indice, nuevo_vehiculo):
        if 0 <= indice < len(self.vehiculos):
            self.vehiculos[indice] = nuevo_vehiculo
            print("Vehículo editado exitosamente.")
        else:
            print("Índice inválido.")


def main():
    gestion = GestionVehiculos()

    while True:
        print("\n--- Gestión de Vehículos ---")
        print("1. Agregar vehículo")
        print("2. Listar vehículos")
        print("3. Editar vehículo")
        print("4. Eliminar vehículo")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tipo = input("Ingrese el tipo de vehículo (coche/camioneta/bicicleta/motocicleta): ").strip().lower()
            color = input("Color: ")
            ruedas = int(input("Número de ruedas: "))

            if tipo == "coche":
                velocidad = int(input("Velocidad (km/h): "))
                cilindrada = int(input("Cilindrada (cc): "))
                vehiculo = Coche(color, ruedas, velocidad, cilindrada)

            elif tipo == "camioneta":
                velocidad = int(input("Velocidad (km/h): "))
                cilindrada = int(input("Cilindrada (cc): "))
                carga = int(input("Carga (kg): "))
                vehiculo = Camioneta(color, ruedas, velocidad, cilindrada, carga)

            elif tipo == "bicicleta":
                tipo_bici = input("Tipo (urbana/deportiva): ")
                vehiculo = Bicicleta(color, ruedas, tipo_bici)

            elif tipo == "motocicleta":
                tipo_bici = input("Tipo (urbana/deportiva): ")
                velocidad = int(input("Velocidad (km/h): "))
                cilindrada = int(input("Cilindrada (cc): "))
                vehiculo = Motocicleta(color, ruedas, tipo_bici, velocidad, cilindrada)

            else:
                print("Tipo de vehículo no válido.")
                continue

            gestion.agregar_vehiculo(vehiculo)

        elif opcion == "2":
            gestion.listar_vehiculos()

        elif opcion == "3":
            gestion.listar_vehiculos()
            indice = int(input("Seleccione el número del vehículo a editar: ")) - 1
            tipo = input("Ingrese el nuevo tipo de vehículo (coche/camioneta/bicicleta/motocicleta): ").strip().lower()
            color = input("Nuevo color: ")
            ruedas = int(input("Nuevo número de ruedas: "))

            if tipo == "coche":
                velocidad = int(input("Nueva velocidad (km/h): "))
                cilindrada = int(input("Nueva cilindrada (cc): "))
                nuevo_vehiculo = Coche(color, ruedas, velocidad, cilindrada)

            elif tipo == "camioneta":
                velocidad = int(input("Nueva velocidad (km/h): "))
                cilindrada = int(input("Nueva cilindrada (cc): "))
                carga = int(input("Nueva carga (kg): "))
                nuevo_vehiculo = Camioneta(color, ruedas, velocidad, cilindrada, carga)

            elif tipo == "bicicleta":
                tipo_bici = input("Nuevo tipo (urbana/deportiva): ")
                nuevo_vehiculo = Bicicleta(color, ruedas, tipo_bici)

            elif tipo == "motocicleta":
                tipo_bici = input("Nuevo tipo (urbana/deportiva): ")
                velocidad = int(input("Nueva velocidad (km/h): "))
                cilindrada = int(input("Nueva cilindrada (cc): "))
                nuevo_vehiculo = Motocicleta(color, ruedas, tipo_bici, velocidad, cilindrada)

            else:
                print("Tipo de vehículo no válido.")
                continue

            gestion.editar_vehiculo(indice, nuevo_vehiculo)

        elif opcion == "4":
            gestion.listar_vehiculos()
            indice = int(input("Seleccione el número del vehículo a eliminar: ")) - 1
            gestion.eliminar_vehiculo(indice)

        elif opcion == "5":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()

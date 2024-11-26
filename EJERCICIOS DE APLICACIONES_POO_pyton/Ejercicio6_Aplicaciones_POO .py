#Diseñe un algoritmo empleando Python, POO y sus propiedades (herencia, encapsulamiento y polimorfismo)
#en la solución de un problema que involucre la ingeniería electrónica. Puede buscar una asignatura de 
#su pensum para realizar una aplicación.
# Clase base
class DispositivoElectronico:
    def __init__(self, nombre, modelo, ubicacion):
        self.nombre = nombre
        self.modelo = modelo
        self.ubicacion = ubicacion

    def mostrar_info(self):
        """Muestra información general del dispositivo"""
        print(f"Nombre: {self.nombre}")
        print(f"Modelo: {self.modelo}")
        print(f"Ubicación: {self.ubicacion}")

class Sensor(DispositivoElectronico):
    def __init__(self, nombre, modelo, ubicacion, tipo, rango):
        super().__init__(nombre, modelo, ubicacion)
        self.tipo = tipo
        self.rango = rango

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de sensor: {self.tipo}")
        print(f"Rango de medición: {self.rango}")

class Actuador(DispositivoElectronico):
    def __init__(self, nombre, modelo, ubicacion, tipo, potencia):
        super().__init__(nombre, modelo, ubicacion)
        self.tipo = tipo
        self.potencia = potencia

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de actuador: {self.tipo}")
        print(f"Potencia máxima: {self.potencia}")


class Controlador(DispositivoElectronico):
    def __init__(self, nombre, modelo, ubicacion, protocolo):
        super().__init__(nombre, modelo, ubicacion)
        self.protocolo = protocolo

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Protocolo de comunicación: {self.protocolo}")


class GestionDispositivos:
    def __init__(self):
        self.dispositivos = []

    def agregar_dispositivo(self):
        print("\nAgregar Dispositivo ")
        print("1. Sensor")
        print("2. Actuador")
        print("3. Controlador")
        opcion = int(input("Seleccione el tipo de dispositivo: "))
        
        nombre = input("Nombre del dispositivo: ")
        modelo = input("Modelo: ")
        ubicacion = input("Ubicación: ")
        
        if opcion == 1:
            tipo = input("Tipo de sensor: ")
            rango = input("Rango de medición: ")
            dispositivo = Sensor(nombre, modelo, ubicacion, tipo, rango)
        elif opcion == 2:
            tipo = input("Tipo de actuador: ")
            potencia = input("Potencia máxima: ")
            dispositivo = Actuador(nombre, modelo, ubicacion, tipo, potencia)
        elif opcion == 3:
            protocolo = input("Protocolo de comunicación: ")
            dispositivo = Controlador(nombre, modelo, ubicacion, protocolo)
        else:
            print("Opción inválida. Regresando al menú.")
            return

        self.dispositivos.append(dispositivo)
        print("Dispositivo agregado con éxito.")

    def listar_dispositivos(self):
        print("\n Lista de Dispositivos ")
        if not self.dispositivos:
            print("No hay dispositivos registrados.")
            return
        
        for i, dispositivo in enumerate(self.dispositivos, 1):
            print(f"\nDispositivo {i}:")
            dispositivo.mostrar_info()
            print("-" * 30)

    def menu(self):
        while True:
            print("\n--- Menú de Gestión de Dispositivos ---")
            print("1. Agregar dispositivo")
            print("2. Listar dispositivos")
            print("3. Salir")
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                self.agregar_dispositivo()
            elif opcion == 2:
                self.listar_dispositivos()
            elif opcion == 3:
                print("Saliendo del programa.")
                break
            else:
                print("Opción inválida. Intente de nuevo.")


gestion = GestionDispositivos()
gestion.menu()

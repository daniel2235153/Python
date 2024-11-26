#Diseñe un programa aplicando POO para un concesionario de autos 
# (automóviles, camionetas, camiones, tractocamiones), tenga en cuenta las 
# características en común y cree las clases necesarias, por ejemplo modelos, 
# tipo de pintura, cantidades de unidades en inventario. 
class Concesionario:
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self):
        print("Seleccione el tipo de vehículo:")
        print("1. Automóvil")
        print("2. Camioneta")
        print("3. Camión")
        print("4. Tractocamión")
        tipo = int(input("Digite la opción: "))
        
        if tipo == 1:
            tipo_vehiculo = "Automóvil"
        elif tipo == 2:
            tipo_vehiculo = "Camioneta"
        elif tipo == 3:
            tipo_vehiculo = "Camión"
        elif tipo == 4:
            tipo_vehiculo = "Tractocamión"
        else:
            print("Opción inválida.")
            self.agregar_vehiculo()
            return

        modelo = input("Digite el modelo del vehículo: ")
        pintura = input("Digite el tipo de pintura (brillante/mate): ")
        unidades = int(input("Digite la cantidad de unidades en inventario: "))

        self.vehiculos.append({
            "Tipo": tipo_vehiculo,
            "Modelo": modelo,
            "Pintura": pintura,
            "Unidades": unidades
        })
        print("Vehículo agregado con éxito.")
        self.menu()

    def buscar_vehiculo(self):
        modelo = input("Digite el modelo del vehículo que desea buscar: ")
        encontrado = False
        for vehiculo in self.vehiculos:
            if vehiculo["Modelo"].lower() == modelo.lower():
                print("Tipo: ", vehiculo["Tipo"])
                print("Modelo: ", vehiculo["Modelo"])
                print("Pintura: ", vehiculo["Pintura"])
                print("Unidades: ", vehiculo["Unidades"])
                encontrado = True
        if not encontrado:
            print("El vehículo no se encuentra en el inventario.")
        self.menu()

    def listar_vehiculos(self):
        print("Tipo\t\tModelo\t\tPintura\t\tUnidades")
        for vehiculo in self.vehiculos:
            print(f"{vehiculo['Tipo']}\t\t{vehiculo['Modelo']}\t\t{vehiculo['Pintura']}\t\t{vehiculo['Unidades']}")
        self.menu()

    def editar_vehiculo(self):
        modelo = input("Digite el modelo del vehículo que desea editar: ")
        for vehiculo in self.vehiculos:
            if vehiculo["Modelo"].lower() == modelo.lower():
                print('''¿Qué desea editar?
                        1. Modelo
                        2. Tipo de pintura
                        3. Cantidad de unidades''')
                opcion = int(input("Digite una opción: "))
                if opcion == 1:
                    nuevo_modelo = input("Digite el nuevo modelo: ")
                    vehiculo["Modelo"] = nuevo_modelo
                    print("Modelo actualizado.")
                elif opcion == 2:
                    nueva_pintura = input("Digite el nuevo tipo de pintura: ")
                    vehiculo["Pintura"] = nueva_pintura
                    print("Pintura actualizada.")
                elif opcion == 3:
                    nuevas_unidades = int(input("Digite la nueva cantidad de unidades: "))
                    vehiculo["Unidades"] = nuevas_unidades
                    print("Cantidad de unidades actualizada.")
                else:
                    print("Opción inválida.")
                self.menu()
                return
        print("El vehículo no se encuentra en el inventario.")
        self.menu()

    def eliminar_vehiculo(self):
        modelo = input("Digite el modelo del vehículo que desea eliminar: ")
        for vehiculo in self.vehiculos:
            if vehiculo["Modelo"].lower() == modelo.lower():
                self.vehiculos.remove(vehiculo)
                print("Vehículo eliminado del inventario.")
                self.menu()
                return
        print("El vehículo no se encuentra en el inventario.")
        self.menu()

    def menu(self):
        print('''CONCESIONARIO
                    Opciones:
                    1. Agregar vehículo
                    2. Buscar vehículo
                    3. Listar vehículos
                    4. Editar vehículo
                    5. Eliminar vehículo''')
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            self.agregar_vehiculo()
        elif opcion == 2:
            self.buscar_vehiculo()
        elif opcion == 3:
            self.listar_vehiculos()
        elif opcion == 4:
            self.editar_vehiculo()
        elif opcion == 5:
            self.eliminar_vehiculo()
        else:
            print("Opción inválida.")
            self.menu()

concesionario = Concesionario()
concesionario.menu()

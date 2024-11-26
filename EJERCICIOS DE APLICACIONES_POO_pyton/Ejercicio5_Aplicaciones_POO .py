# Se requiere diseñar un programa mediante Python y POO, que satisfaga la siguiente situación: Una empresa requiere implementar un sistema
#  de información donde se encuentren todos sus empleados y visitantes con los siguientes datos (código empleado, apellidos, nombres, 
# # documento, área de trabajo (seguridad, servicios generales, administrativo, auxiliar o visitante), hora de ingreso, temperatura de ingreso
#  °C, hora de salida, temperatura de salida °C). Su programa debe tener la posibilidad de establecer las clases necesarias con sus atributos 
# y métodos para lograr: aceptar el ingreso de información según requerimientos, editar la información cuando sea necesaria, eliminar usuarios
#  que ya no pertenezcan a la empresa, hacer búsquedas de empleados o visitantes teniendo en cuenta los siguientes criterios: mostrar nombre y 
# apellidos de usuarios que tengan temperatura mayor a 37.5°C, por cargo dentro de la empresa o visitantes, por hora de llegada y por hora de salida.
#  Además, su programa debe enviar alertas en pantalla donde establezca un mensaje de que algún empleado esta por arriba de 38°C en la medición 
# de su temperatura.
class Empresa:
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self):
        codigo = input("Digite el código del empleado/visitante: ")
        apellidos = input("Digite los apellidos: ")
        nombres = input("Digite los nombres: ")
        documento = input("Digite el número de documento: ")
        area = input("Digite el área de trabajo (seguridad, servicios generales, administrativo, auxiliar o visitante): ")
        hora_ingreso = input("Digite la hora de ingreso (HH:MM): ")
        temperatura_ingreso = float(input("Digite la temperatura de ingreso °C: "))
        hora_salida = input("Digite la hora de salida (HH:MM): ")
        temperatura_salida = float(input("Digite la temperatura de salida °C: "))

        if temperatura_ingreso > 38.0:
            print("¡ALERTA! El empleado tiene una temperatura crítica al ingreso.")

        self.usuarios.append({
            "Codigo": codigo,
            "Apellidos": apellidos,
            "Nombres": nombres,
            "Documento": documento,
            "Área": area,
            "Hora Ingreso": hora_ingreso,
            "Temperatura Ingreso": temperatura_ingreso,
            "Hora Salida": hora_salida,
            "Temperatura Salida": temperatura_salida
        })
        print("Usuario agregado con éxito.")
        self.menu()

    def buscar_usuario(self):
        print('''Opciones de búsqueda:
        1. Por temperatura (> 37.5°C)
        2. Por cargo/visitante
        3. Por hora de llegada
        4. Por hora de salida''')
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            for usuario in self.usuarios:
                if usuario["Temperatura Ingreso"] > 37.5 or usuario["Temperatura Salida"] > 37.5:
                    print(f"{usuario['Nombres']} {usuario['Apellidos']} tiene temperatura mayor a 37.5°C.")
        elif opcion == 2:
            cargo = input("Digite el cargo/visitante a buscar: ")
            for usuario in self.usuarios:
                if usuario["Área"].lower() == cargo.lower():
                    print(f"{usuario['Nombres']} {usuario['Apellidos']} - {usuario['Área']}")
        elif opcion == 3:
            hora = input("Digite la hora de llegada (HH:MM): ")
            for usuario in self.usuarios:
                if usuario["Hora Ingreso"] == hora:
                    print(f"{usuario['Nombres']} {usuario['Apellidos']} llegó a las {hora}.")
        elif opcion == 4:
            hora = input("Digite la hora de salida (HH:MM): ")
            for usuario in self.usuarios:
                if usuario["Hora Salida"] == hora:
                    print(f"{usuario['Nombres']} {usuario['Apellidos']} salió a las {hora}.")
        else:
            print("Opción no válida.")
        self.menu()

    def editar_usuario(self):
        documento = input("Digite el documento del usuario que desea editar: ")
        for usuario in self.usuarios:
            if usuario["Documento"] == documento:
                print("Usuario encontrado. ¿Qué desea editar?")
                print("1. Apellidos\n2. Nombres\n3. Área\n4. Hora de ingreso\n5. Temperatura de ingreso\n6. Hora de salida\n7. Temperatura de salida")
                opcion = int(input("Seleccione una opción: "))

                if opcion == 1:
                    usuario["Apellidos"] = input("Digite los nuevos apellidos: ")
                elif opcion == 2:
                    usuario["Nombres"] = input("Digite los nuevos nombres: ")
                elif opcion == 3:
                    usuario["Área"] = input("Digite la nueva área: ")
                elif opcion == 4:
                    usuario["Hora Ingreso"] = input("Digite la nueva hora de ingreso (HH:MM): ")
                elif opcion == 5:
                    usuario["Temperatura Ingreso"] = float(input("Digite la nueva temperatura de ingreso °C: "))
                elif opcion == 6:
                    usuario["Hora Salida"] = input("Digite la nueva hora de salida (HH:MM): ")
                elif opcion == 7:
                    usuario["Temperatura Salida"] = float(input("Digite la nueva temperatura de salida °C: "))
                print("Usuario editado con éxito.")
                break
        else:
            print("Usuario no encontrado.")
        self.menu()

    def eliminar_usuario(self):
        documento = input("Digite el documento del usuario que desea eliminar: ")
        for usuario in self.usuarios:
            if usuario["Documento"] == documento:
                self.usuarios.remove(usuario)
                print("Usuario eliminado con éxito.")
                break
        else:
            print("Usuario no encontrado.")
        self.menu()

    def listar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios registrados.")
        else:
            print("Usuarios registrados:")
            for usuario in self.usuarios:
                print(f"{usuario['Nombres']} {usuario['Apellidos']} - {usuario['Área']}")
        self.menu()

    def menu(self):
        print('''Menú Principal
        1. Agregar usuario
        2. Buscar usuario
        3. Editar usuario
        4. Eliminar usuario
        5. Listar usuarios
        6. Salir''')
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            self.agregar_usuario()
        elif opcion == 2:
            self.buscar_usuario()
        elif opcion == 3:
            self.editar_usuario()
        elif opcion == 4:
            self.eliminar_usuario()
        elif opcion == 5:
            self.listar_usuarios()
        elif opcion == 6:
            print("¡Hasta luego!")
        else:
            print("Opción no válida.")
            self.menu()

empresa = Empresa()
empresa.menu()

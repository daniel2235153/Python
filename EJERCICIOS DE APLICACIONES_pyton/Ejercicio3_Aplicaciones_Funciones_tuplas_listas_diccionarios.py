#Modifique el programa anterior, ahora por medio de listas edite por pantalla los datos de las personas, 
#cambie dirección y teléfono.
B_datos = [
    ["Juan", "Pérez", "12345678", "Calle 123 #45-67", "3001234567"],
    ["Luis", "Rodríguez", "11223344", "Avenida 89 #12-34", "3201122334"],
    ["Ana", "Martínez", "55667788", "Transversal 78 #56-78", "3005566778"],
]

def mostrar_base_datos(base_datos):
    print(f"{'Nombre':<15}{'Apellido':<15}{'Documento':<15}{'Dirección':<25}{'Teléfono':<15}")
    for persona in base_datos:
        print(f"{persona[0]:<15}{persona[1]:<15}{persona[2]:<15}{persona[3]:<25}{persona[4]:<15}")

def editar_datos(base_datos):
    documento = input("Ingrese el documento de la persona a modificar: ")
    for i, persona in enumerate(base_datos):
        if persona[2] == documento:
            nueva_direccion = input("Ingrese la nueva dirección: ")
            nuevo_telefono = input("Ingrese el nuevo teléfono: ")
            base_datos[i][3] = nueva_direccion
            base_datos[i][4] = nuevo_telefono
            print("Datos actualizados correctamente.")
            return
    print("No se encontró ninguna persona con ese documento.")

mostrar_base_datos(B_datos)
editar_datos(B_datos)
mostrar_base_datos(B_datos)
#Aplicando tuplas, diseñe una base de datos que permita visualizar 
# nombres, apellidos, documento de identidad, dirección de residencia y número de teléfono.
base_datos = [
    ("Juan", "Pérez", "12345678", "Calle 123 #45-67", "3001234567"),
    ("Luis", "Rodríguez", "11223344", "Avenida 89 #12-34", "3201122334"),
    ("Ana", "Martínez", "55667788", "Transversal 78 #56-78", "3005566778"),
]
def mostrar_base_datos(base_datos):
    print(f"{'Nombre':<15}{'Apellido':<15}{'Documento':<15}{'Dirección':<15}{'Teléfono':<15}")
    for registro in base_datos:
        nombre, apellido, documento, direccion, telefono = registro
        print(f"{nombre:<15}{apellido:<15}{documento:<15}{direccion:<25}{telefono:<15}")
mostrar_base_datos(base_datos)

#Diseñe un algoritmo que le permita crear una lista con nombres de estudiantes 
# (N nombres), su programa debe permitir buscar si los nombres están contenidos en la lista, 
# la consulta solicita nombres y verifica si están o no. 
estudiantes = []

def crear_lista_E():
    print("Digite los nombres de los estudiantes. Escribe 'F' para terminar.")
    while True:
        nombre = input("Nombre del estudiante: ").strip()
        if nombre.upper() == "F":
            break
        if nombre: 
            estudiantes.append(nombre)
    print("\nLista de estudiantes creada:")
    print(estudiantes)

def buscar_N():
    print("\nDigite los nombres que deseas buscar. Escribe 'F' para terminar.")
    while True:
        Buscar_nom = input("Nombre a buscar: ").strip()
        if Buscar_nom.upper() == "F":
            break
        if Buscar_nom in estudiantes:
            print(f"El nombre '{Buscar_nom}' está en la lista.")
        else:
            print(f"El nombre '{Buscar_nom}' NO está en la lista.")
def main():
    print("=== GESTIÓN DE NOMBRES DE ESTUDIANTES ===")
    crear_lista_E()
    buscar_N()

main()

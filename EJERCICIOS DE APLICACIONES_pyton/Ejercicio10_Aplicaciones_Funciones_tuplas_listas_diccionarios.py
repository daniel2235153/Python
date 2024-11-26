import time
parqueadero = {}
def registrar_entrada():
    print("\n=== REGISTRAR ENTRADA ===")
    codigo = input("Código del vehículo (5 dígitos): ").strip()
    if codigo in parqueadero:
        print("El vehículo ya está registrado.")
    else:
        tipo = input("Tipo de vehículo (carro/moto): ").strip().lower()
        if tipo in ["carro", "moto"]:
            parqueadero[codigo] = {"tipo": tipo, "hora_entrada": time.time()}
            print(f"Entrada registrada para {tipo} con código {codigo}.")
        else:
            print("Tipo de vehículo inválido.")

def registrar_salida():
    print("\n=== REGISTRAR SALIDA ===")
    codigo = input("Código del vehículo (5 dígitos): ").strip()
    if codigo in parqueadero:
        datos = parqueadero[codigo]
        tiempo = (time.time() - datos["hora_entrada"]) / 3600
        tarifa = 2000 if datos["tipo"] == "moto" else 5000
        print(f"El vehículo {datos['tipo']} con código {codigo} estuvo {tiempo:.2f} horas.")
        print(f"Total a pagar: ${round(tiempo * tarifa, 2):.2f}")
        del parqueadero[codigo]
    else:
        print("El vehículo no está registrado.")

def listar_vehiculos():
    print("\n=== VEHÍCULOS REGISTRADOS ===")
    if parqueadero:
        for codigo, datos in parqueadero.items():
            hora = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(datos["hora_entrada"]))
            print(f"Código: {codigo}, Tipo: {datos['tipo']}, Entrada: {hora}")
    else:
        print("No hay vehículos registrados.")

def main():
    while True:
        print("\n1. Registrar entrada")
        print("2. Registrar salida")
        print("3. Listar vehículos")
        print("4. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            registrar_entrada()
        elif opcion == "2":
            registrar_salida()
        elif opcion == "3":
            listar_vehiculos()
        elif opcion == "4":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

main()

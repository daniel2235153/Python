import pandas as pd
from datetime import datetime, timedelta
import re

class Biblioteca:
    def __init__(self):
        # Archivos por defecto
        self.archivos = {
            'libros': 'Archivos/libros.csv',
            'usuarios': 'Archivos/usuarios.csv',
            'prestamos': 'Archivos/prestamos.csv'
        }
        # Credenciales del administrador
        self.admin_credentials = {'usuario': 'admin', 'contraseña': 'admin1'}

        # Cargar o crear archivos
        self.df_libros = self.cargar_dataframe(self.archivos['libros'], ['Código', 'Autor', 'Tema', 'Páginas', 'Cantidad', 'Precio'])
        self.df_usuarios = self.cargar_dataframe(self.archivos['usuarios'], ['Nombre', 'Clave'])
        self.df_prestamos = self.cargar_dataframe(self.archivos['prestamos'], ['Usuario', 'Código Libro', 'Fecha Préstamo', 'Fecha Entrega', 'Devuelto'])

    def cargar_dataframe(self, archivo, columnas):
        """Carga un CSV o crea uno nuevo si no existe."""
        try:
            return pd.read_csv(archivo)
        except FileNotFoundError:
            df = pd.DataFrame(columns=columnas)
            df.to_csv(archivo, index=False)
            return df

    def validar_codigo(self, codigo):
        """Valida que el código sea alfanumérico y tenga exactamente 6 caracteres"""
        return bool(re.match(r'^[A-Za-z0-9]{6}$', codigo))

    def agregar_libro(self):
        codigo = input("Ingrese el código del libro (alfanumérico de 6 caracteres): ")
        if not self.validar_codigo(codigo): return print("Código inválido.")
        
        libro = {
            'Código': codigo,
            'Autor': input("Autor: "),
            'Tema': input("Tema: "),
            'Páginas': int(input("Número de páginas: ")),
            'Cantidad': int(input("Cantidad de ejemplares: ")),
            'Precio': float(input("Precio: "))
        }
        self.df_libros = self.df_libros.append(libro, ignore_index=True)
        self.df_libros.to_csv(self.archivos['libros'], index=False)
        print("Libro agregado correctamente.")

    def eliminar_libro(self):
        codigo = input("Ingrese el código del libro a eliminar: ")
        if codigo in self.df_libros['Código'].values:
            self.df_libros = self.df_libros[self.df_libros['Código'] != codigo]
            self.df_libros.to_csv(self.archivos['libros'], index=False)
            print("Libro eliminado correctamente.")
        else:
            print("Libro no encontrado.")

    def agregar_usuario(self):
        usuario = {
            'Nombre': input("Ingrese nombre del usuario: "),
            'Clave': input("Ingrese clave de seguridad: ")
        }
        self.df_usuarios = self.df_usuarios.append(usuario, ignore_index=True)
        self.df_usuarios.to_csv(self.archivos['usuarios'], index=False)
        print("Usuario agregado correctamente.")

    def verificar_usuario(self):
        nombre = input("Nombre: ")
        clave = input("Clave: ")
        if not self.df_usuarios[(self.df_usuarios['Nombre'] == nombre) & (self.df_usuarios['Clave'] == clave)].empty:
            return nombre
        print("Usuario o clave incorrectos.")
        return None

    def verificar_admin(self):
        usuario = input("Usuario admin: ")
        contraseña = input("Contraseña admin: ")
        if usuario == self.admin_credentials['usuario'] and contraseña == self.admin_credentials['contraseña']:
            return True
        print("Acceso de administrador denegado.")
        return False

    def prestar_libro(self):
        usuario = self.verificar_usuario()
        if not usuario: return
        
        codigo_libro = input("Código del libro: ")
        if codigo_libro in self.df_libros['Código'].values:
            libro = self.df_libros[self.df_libros['Código'] == codigo_libro].iloc[0]
            if libro['Cantidad'] > 0:
                fecha_prestamo = datetime.now()
                fecha_entrega = fecha_prestamo + timedelta(days=15)
                prestamo = {
                    'Usuario': usuario,
                    'Código Libro': codigo_libro,
                    'Fecha Préstamo': fecha_prestamo.strftime('%Y-%m-%d'),
                    'Fecha Entrega': fecha_entrega.strftime('%Y-%m-%d'),
                    'Devuelto': False
                }
                self.df_prestamos = self.df_prestamos.append(prestamo, ignore_index=True)
                self.df_libros.loc[self.df_libros['Código'] == codigo_libro, 'Cantidad'] -= 1
                self.df_libros.to_csv(self.archivos['libros'], index=False)
                self.df_prestamos.to_csv(self.archivos['prestamos'], index=False)
                print(f"Libro prestado. Fecha de entrega: {fecha_entrega.strftime('%Y-%m-%d')}")
            else:
                print("No hay ejemplares disponibles.")
        else:
            print("Código de libro no encontrado.")

    def consultar_prestamos(self, usuario=None):
        if usuario:
            prestamos = self.df_prestamos[(self.df_prestamos['Usuario'] == usuario) & (self.df_prestamos['Devuelto'] == False)]
        else:
            prestamos = self.df_prestamos[self.df_prestamos['Devuelto'] == False]
        
        if prestamos.empty:
            print("No hay préstamos pendientes.")
        else:
            print(prestamos[['Usuario', 'Código Libro', 'Fecha Préstamo', 'Fecha Entrega']])

    def mostrar_libros(self):
        if self.verificar_admin():
            print(self.df_libros)

    def menu(self):
        opciones = {
            '1': self.agregar_libro,
            '2': self.eliminar_libro,
            '3': self.agregar_usuario,
            '4': self.prestar_libro,
            '5': self.consultar_prestamos,
            '6': self.consultar_prestamos,
            '7': self.mostrar_libros,
            '8': exit
        }
        while True:
            print("\nMenú:")
            print("1. Agregar Libro")
            print("2. Eliminar Libro")
            print("3. Agregar Usuario")
            print("4. Prestar Libro")
            print("5. Consultar Préstamos (Usuario)")
            print("6. Consultar Préstamos (Administrador)")
            print("7. Mostrar Información de Libros (Administrador)")
            print("8. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion in opciones:
                if opcion == '5':  # Consultar préstamos por usuario
                    usuario = self.verificar_usuario()
                    if usuario:
                        self.consultar_prestamos(usuario)
                elif opcion == '6':  # Consultar préstamos por administrador
                    if self.verificar_admin():
                        self.consultar_prestamos()
                else:
                    opciones[opcion]()

if __name__ == '__main__':
    biblioteca = Biblioteca()
    biblioteca.menu()

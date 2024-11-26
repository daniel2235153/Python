import tkinter as tk
from tkinter import ttk, messagebox
import csv
from collections import defaultdict

class CinemaManager:
    def __init__(self):
        self.cartelera = []  
        self.ventas_tiquetes = defaultdict(int) 
        self.ventas_comida = defaultdict(float)  
        self.ganancias_peliculas = defaultdict(float)  

        self.cargar_cartelera()
        self.cargar_ventas()

    def cargar_cartelera(self):
        try:
            with open("cartelera.csv", "r") as file:
                reader = csv.reader(file)
                self.cartelera = [row for row in reader]
        except FileNotFoundError:
            self.cartelera = []  

    def cargar_ventas(self):
        try:
            with open("ventas.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    tipo, nombre, cantidad, total = row
                    cantidad, total = int(cantidad), float(total)
                    if tipo == "Película":
                        self.ventas_tiquetes[nombre] += cantidad
                        self.ganancias_peliculas[nombre] += total
                    elif tipo == "Comida":
                        self.ventas_comida[nombre] += total
        except FileNotFoundError:
            pass  

    def guardar_venta(self, tipo, nombre, cantidad, total):
        with open("ventas.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([tipo, nombre, cantidad, total])

    def mostrar_cartelera(self):
        return "\n".join([f"{nombre} - {horario}" for nombre, horario in self.cartelera])

    def vender_tiquete(self, pelicula, cantidad, precio_unitario):
        total = cantidad * precio_unitario
        self.ventas_tiquetes[pelicula] += cantidad
        self.ganancias_peliculas[pelicula] += total
        self.guardar_venta("Película", pelicula, cantidad, total)
        return total

    def vender_comida(self, comida, cantidad, precio_unitario):
        total = cantidad * precio_unitario
        self.ventas_comida[comida] += total
        self.guardar_venta("Comida", comida, cantidad, total)
        return total

    def generar_informe(self):
        informe = ["Informe de Ventas:"]
        informe.append("\nTiquetes vendidos por película:")
        for pelicula, cantidad in self.ventas_tiquetes.items():
            informe.append(f"  {pelicula}: {cantidad} tiquetes vendidos, ${self.ganancias_peliculas[pelicula]:.2f} recaudados")
        informe.append("\nDinero ganado en venta de comida:")
        for comida, total in self.ventas_comida.items():
            informe.append(f"  {comida}: ${total:.2f}")
        return "\n".join(informe)

class CinemaApp:
    def __init__(self, root):
        self.manager = CinemaManager()
        self.root = root
        self.root.title("Gestión de Cinema")

        self.tab_control = ttk.Notebook(root)
        self.tab_cartelera = ttk.Frame(self.tab_control)
        self.tab_tiquetes = ttk.Frame(self.tab_control)
        self.tab_comidas = ttk.Frame(self.tab_control)
        self.tab_informe = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab_cartelera, text="Cartelera")
        self.tab_control.add(self.tab_tiquetes, text="Venta de Tiquetes")
        self.tab_control.add(self.tab_comidas, text="Venta de Comidas")
        self.tab_control.add(self.tab_informe, text="Informe")
        self.tab_control.pack(expand=1, fill="both")

        self.crear_tabla_cartelera()
        self.crear_tabla_tiquetes()
        self.crear_tabla_comidas()
        self.crear_tabla_informe()

    def crear_tabla_cartelera(self):
        label = tk.Label(self.tab_cartelera, text="Cartelera de Películas", font=("Arial", 14))
        label.pack(pady=10)
        text = tk.Text(self.tab_cartelera, height=15, width=50)
        text.insert(tk.END, self.manager.mostrar_cartelera())
        text.configure(state="disabled")
        text.pack()

    def crear_tabla_tiquetes(self):
        label = tk.Label(self.tab_tiquetes, text="Venta de Tiquetes", font=("Arial", 14))
        label.pack(pady=10)

        tk.Label(self.tab_tiquetes, text="Película:").pack()
        self.entry_pelicula = ttk.Combobox(self.tab_tiquetes, values=[p[0] for p in self.manager.cartelera])
        self.entry_pelicula.pack()

        tk.Label(self.tab_tiquetes, text="Cantidad:").pack()
        self.entry_cantidad = tk.Entry(self.tab_tiquetes)
        self.entry_cantidad.pack()

        tk.Label(self.tab_tiquetes, text="Precio Unitario:").pack()
        self.entry_precio = tk.Entry(self.tab_tiquetes)
        self.entry_precio.pack()

        btn = tk.Button(self.tab_tiquetes, text="Vender", command=self.vender_tiquete)
        btn.pack(pady=10)

    def crear_tabla_comidas(self):
        label = tk.Label(self.tab_comidas, text="Venta de Comidas", font=("Arial", 14))
        label.pack(pady=10)

        tk.Label(self.tab_comidas, text="Producto:").pack()
        self.entry_comida = tk.Entry(self.tab_comidas)
        self.entry_comida.pack()

        tk.Label(self.tab_comidas, text="Cantidad:").pack()
        self.entry_cantidad_comida = tk.Entry(self.tab_comidas)
        self.entry_cantidad_comida.pack()

        tk.Label(self.tab_comidas, text="Precio Unitario:").pack()
        self.entry_precio_comida = tk.Entry(self.tab_comidas)
        self.entry_precio_comida.pack()

        btn = tk.Button(self.tab_comidas, text="Vender", command=self.vender_comida)
        btn.pack(pady=10)

    def crear_tabla_informe(self):
        label = tk.Label(self.tab_informe, text="Informe para Administrador", font=("Arial", 14))
        label.pack(pady=10)

        btn = tk.Button(self.tab_informe, text="Generar Informe", command=self.mostrar_informe)
        btn.pack(pady=10)

        self.text_informe = tk.Text(self.tab_informe, height=20, width=60)
        self.text_informe.pack()

    def vender_tiquete(self):
        pelicula = self.entry_pelicula.get()
        cantidad = int(self.entry_cantidad.get())
        precio = float(self.entry_precio.get())
        total = self.manager.vender_tiquete(pelicula, cantidad, precio)
        messagebox.showinfo("Venta Exitosa", f"Tiquetes vendidos. Total: ${total:.2f}")

    def vender_comida(self):
        comida = self.entry_comida.get()
        cantidad = int(self.entry_cantidad_comida.get())
        precio = float(self.entry_precio_comida.get())
        total = self.manager.vender_comida(comida, cantidad, precio)
        messagebox.showinfo("Venta Exitosa", f"Comida vendida. Total: ${total:.2f}")

    def mostrar_informe(self):
        informe = self.manager.generar_informe()
        self.text_informe.delete(1.0, tk.END)
        self.text_informe.insert(tk.END, informe)


root = tk.Tk()
app = CinemaApp(root)
root.mainloop()

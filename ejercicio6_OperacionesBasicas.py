#Escriba un programa que pida una temperatura en grados Fahrenheit y que escriba esa temperatura en grados Kelvin
import math
print("Ingrese la temperatura en grados Fahrenheit")
tem=float(input())
kel=(9/5)*(tem-32) + 273.15
print("Temperatura en Kelvin ", kel )
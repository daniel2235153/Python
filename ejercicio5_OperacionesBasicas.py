#Escriba un programa que pida una temperatura en grados Fahrenheit y que escriba esa temperatura en grados Celsius. 
# La relación entre grados Celsius (C) y grados Fahrenheit (F) es la siguiente: C = (F - 32) / 1,8
import math
print("Ingrese la temperatura en grados Fahrenheit")
tem=float(input())

print("Temperatura en Celsius ",(tem-32) * 5/9)
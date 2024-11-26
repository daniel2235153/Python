#Escriba un programa que pida una cantidad de segundos y que escriba cuántas horas, minutos y segundos son:
import math
print("Dijite una cantidad de segunos")
seg = float(input())
min = seg * (1/60)
hor = min* (1/60)
print("segundos:", seg ,"\nminutos", min,"\nhoras", hor)
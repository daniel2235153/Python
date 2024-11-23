#Escriba un programa en Python que pida el peso (en kilogramos) y la altura (en metros) de una persona y que calcule su índice de masa corporal (imc).
#  imc se calcula con la fórmula imc = peso / altura2
import math
print("Digite su peso en Kg y su altura en m")
peso= float(input())
alt= float(input())
imc= peso/alt**2
print("Su índice de masa corporal es", imc) 

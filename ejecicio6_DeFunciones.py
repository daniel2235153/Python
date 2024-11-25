#Diseñe un programa que permita establecer la relación entre dos números ingresados y se cumplan las siguientes 
#relaciones relación(a,b). Si el primer número es mayor que el segundo, debe devolver "True". Si el primer número es 
# menor que el segundo, debe devolver "False" y Si ambos números son iguales, debe devolver un "Empate".
def relacion(a, b):
  if a > b:
    return "True"
  elif a < b:
    return "False"
  else:
    return "Empate"
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
resultado = relacion(num1, num2)
print("Resultado:", resultado)

    

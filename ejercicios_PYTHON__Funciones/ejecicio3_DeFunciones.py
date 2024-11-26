#Diseñe una función hallar_mayor_menor(a,b) que tome como argumento dos números y devuelva el mayor y menor de ellos.
def hallar_mayor_menor(a,b):
    if a > b:
        print(a," es mayor que  " , b)
    else:
         print(b, "es mayor que ",b)
    return a,b
    
a=float(input("digite el primer numero"))
b=float(input("digite el segundo valor"))
a,b= hallar_mayor_menor(a,b)

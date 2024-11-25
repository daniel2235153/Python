#Definir una función inversa() que calcule la inversión de una cadena.
 #Por ejemplo print palabra_inversa('universidad industrial de santander') 
# su programa entrega 'rednatnas ed lairtsudni dadisrevinu'
def palabra_inversa(cadena):
    invertida=""
    for i in cadena:
        invertida=i + invertida
    return invertida

cadena = input("Ingresa una palabra: ") 
print(palabra_inversa(cadena)) 
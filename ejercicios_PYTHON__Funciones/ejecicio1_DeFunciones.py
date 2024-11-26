#Diseñe una función llamada area_perimtero_rectangulo(base, altura) que devuelva el 
# perimetro y área del rectangulo a partir de una base y una altura.

def area_perimetro_rectangulo(base,altura):
  
    area=base*altura
    perimetro= 2*(base + altura)
    return area,perimetro

base=float(input('ingrese el valor de la base'))
altura=float(input('ingrese el valor de la altura'))
 
area,perimetro=area_perimetro_rectangulo(base,altura)
print(f'area: {area}')
print(f'perimetro: {perimetro}')

area_perimetro_rectangulo(base,altura)



 

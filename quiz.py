# Quiz instrucciones condicionales
"""Dados tres números a, b y c, correspondientes a la longitud de los lados de una figura geométrica, determinar si pueden formar los lados de un triángulo."""

print("------------------------------")
print("----- VERIFICAR TRIANGULO ----")
print("------------------------------")

# input
a = int(input("Ingrese la longitud del lado a: "))
b = int(input("Ingrese la longitud del lado b: "))
c = int(input("Ingrese la longitud del lado c: "))
# processing and output
if a + b > c:
    if a + c > b:
        if c + b > a:
            print("si es un triangulo")
        else:
            print("no puede ser un triangulo")

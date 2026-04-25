def es_par(numero):
    return numero % 2 == 0

num = int(input("Ingrese un número: "))

if es_par(num):
    print("Es par")
else:
    print("Es impar")
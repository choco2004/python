numero = int(input("Ingrese un numero de 5 cifras: "))

billetes = [200, 100, 50, 20, 10, 5, 2, 1]

for billete in billetes:
    cantidad = numero // billete
    print(f"Se necesitan {cantidad} de {billete}")
    numero  %= billete

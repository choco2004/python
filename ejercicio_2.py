numero = input("Ingrese un numero: ")
sum = 0
for n in numero: 
    try:
        sum += int(n)
    except: 
        print("No es un numero")
        break

print("La suma de sus componente es: ", sum)

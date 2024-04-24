def enter_nota(typeNota): 
    return float(input(f"Nota de {typeNota}: "))

def calcular_nota(nota, porcent): 
    return nota*porcent/100

nt = enter_nota("teoría")
np = enter_nota("practica")
ne = enter_nota("examen")

promedio = (calcular_nota(nt, 30)+calcular_nota(np, 40)+calcular_nota(ne, 30))/3

print("El promedio final es: ", promedio)

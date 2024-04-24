sueldo_base = float(input("Ingrese el sueldo base: "))
n_hijos = int(input("Ingrese el numero hijos: "))

bonificacion = 80*n_hijos
monto_pagar = sueldo_base + bonificacion

print("El monto total a pagar es: ", monto_pagar)
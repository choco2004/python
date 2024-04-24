sueldo = float(input("Ingrese el sueldo: "))
interes_banco = float(input("Interes que el banco paga (%): "))

interes_mensual = sueldo * interes_banco/100 * 5
monto_total = sueldo + interes_mensual

print("El monto total sera: ", monto_total)
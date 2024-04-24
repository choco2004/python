sueldo_basico = float(input("Ingrese el sueldo: "))

desc = sueldo_basico * 0.1
bonif = sueldo_basico * 0.2

sueldo_neto = sueldo_basico + bonif - desc

print("El sueldo neto es: ", sueldo_neto)
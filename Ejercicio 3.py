# IMC

peso = float(input("Introduzca su peso (kg) "))
estatura = float(input("Introduzca su estatura (m) "))

imc = float (peso / estatura**2)
print("Tu índice de masa corporal es donde es " + str(round(imc, 2)))




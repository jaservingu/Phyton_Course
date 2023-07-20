class Vehiculo:
    color = "Rojo"
    ruedas = "4"
    Puertas = "5"

class Coche(Vehiculo):
    Velocidad = "Veloz"
    Cilindrada = "150 cc"

Coche()
a = Coche()
print("Su cilindraje es de: " + a.Cilindrada)
print("El color del auto es " + a.color)
print("El auto tiene: " + a.Puertas + " puertas")
print("La velocidad del auto es: " + a.Velocidad)
print("El auto es de " + a.ruedas + " ruedas")



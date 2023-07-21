class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir_datos(self):
        print("Nombre del alumno:", self.nombre)
        print("Nota del alumno:", self.nota)

    def resultado_aprobacion(self):
        if self.nota >= 5:
            print(self.nombre + " ha aprobado con una nota de " + str(self.nota) + " ¡Felicidades!")
        else:
            print(f"{self.nombre} ha reprobado con una nota de {self.nota}. ¡Lo siento!")


nombre_alumno = input("Ingrese el nombre del alumno: ")
nota_alumno = float(input("Ingrese la nota del alumno: "))

alumno = Alumno(nombre_alumno, nota_alumno)
alumno.imprimir_datos()
alumno.resultado_aprobacion()
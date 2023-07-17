bisi = int(input("Ingresa el año: "))
if (bisi % 4 == 0 and bisi % 100 != 0) or bisi % 400 == 0:
    print("El año",bisi, "es bisiesto" )
else:
    print("El año",bisi, "no es bisiesto" )


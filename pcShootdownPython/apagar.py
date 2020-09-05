import os

tiempo = 60
continuar = True
infoOut = ""

def limpiar_pantalla():
    os.system("cls")

def separador():
    print("--------------------------------------------------------------------------------")

def espaciado():
    print("")

while continuar:
    resp = 0
    limpiar_pantalla()
    separador()
    print("Temporizador de apagado -- By R4fF73Z")
    separador()
    espaciado()
    print(
 """    (1) Programar nuevo tiempo de apagado
    (2) Cancelar apagado programado
    (3) Salir""")
    espaciado()
    separador()

    if not infoOut== "":
        print("MSG: " + infoOut)
        separador()
        espaciado()
        infoOut = ""


    resp = input("Seleccione una opción por favor: ")

    if resp == str(1):  
        tiempo = int(input("Seleccione en cuantos minutos se apagará el equipo: "))
        separador()
        infoOut = "El equipo se apagará en " + str(tiempo*60) + " minutos..."
        os.system("shutdown -s -t " + str(tiempo*60))

    elif resp == str(2):
        confirmacion = input("Está seguro de cancelar el temporizador? (s/n): ")
        if confirmacion == "n" or confirmacion == "N":
            pass
        elif confirmacion == "s" or confirmacion == "S":
            os.system("shutdown /a")
            infoOut = "Se ha cancelado el temporizador..."
        else:
            infoOut = "ERROR, no se detectó una respuesta válida..."
    elif resp  == str(3):
        continuar = False
        separador()
        print("Saliendo!, que tenga un excelente día! :D")
        separador()
        espaciado()


    else:
        infoOut = "ERROR, favor de elegír una opción válida!..."

    if not continuar:
        break
limpiar_pantalla




# limpiar_pantalla()
# print(Temporizador de PC!)
# separador()
# print("En cuantos minutos se apagará el pc? ")
# tiempo = input()

# separador()
# # os.system("shutdown -s -t " + tiempo)
# print("El pc se apagará en " + tiempo + "minutos!")
# separador()

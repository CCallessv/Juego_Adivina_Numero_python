import random

def adivina_Numero():
    NumeroSecreto= random.randint(1, 50)
    intentos = 0
    adivinado = False


    print("Hola este es un juego de ADIVINA EL NUMERO ¡BIENVENIDO!")
    print("Debes de adivinar entre el 1 al 50 el numero secreto :D")
    print("!Vamos a intentarlo siuuuuuuuuuuu¡")

    while not adivinado:
        adivinanza = input("Introduzca un numero del 1 al 50: ")

        if adivinanza.isdigit():
            adivinanza = int(adivinanza)
            intentos += 1

            if adivinanza > NumeroSecreto:
                print(f"el numero secreto es menor que {adivinanza}")

            elif adivinanza < NumeroSecreto:
                print(f"el numero secreto es mayor a {adivinanza}")

            else:
                print(f"El numero {adivinanza} es el correcto felicidadessssssssssss siuuuuuuuuuuuuuuuuuuuuu y lo has logrado en {intentos}")
                break
        else:
            print("Por favor introduzca un numero valido :)")        


adivina_Numero()






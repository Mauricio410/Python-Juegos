import random

def crear_palabra_aleatoria():
    palabras=["perro","auto","billete","tractor","edificio","television","tatuaje","elefante","teclado","programacion","universidad","medico"]
    palabras_aleatoria=random.choice(palabras)
    return palabras_aleatoria

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    tablero=""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero+=letra
        else:
            tablero+="_"
    print(tablero)

def jugar_ahorcado():
    palabra_secreta=crear_palabra_aleatoria()
    letras_adivinadas=[]
    intentos_restantes=8
    while intentos_restantes > 0:
        mostrar_tablero(palabra_secreta, letras_adivinadas)
        letra=input("Ingrese una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya has ingresado esta letra, Prueba con otra.")
            continue

        if letra in palabra_secreta:
            letras_adivinadas.append(letra)
            if set(letras_adivinadas)==set(palabra_secreta):
                print("Felicidades, has adivinado la palabra.")
                break
        
        else:
            intentos_restantes -= 1
            print(f"Letra incorrecta. Te quedan {intentos_restantes}")

    if intentos_restantes == 0:
        print(f"Game Over! La palabra secreta era: {palabra_secreta}")

jugar_ahorcado()
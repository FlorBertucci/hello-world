print("Tienes 3 intentos para adivinar el objeto: ")
print("Soy alta y delgada, tengo un ojo, hago vestidos y no me los pongo. ¿Quién soy?")

objeto = str("aguja")
intento = ""
contador_intentos = 0
max_intentos = 3
superar_intentos = False

while intento != objeto and not(superar_intentos):
    if contador_intentos < max_intentos:
        intento = input("Ingrese la palabra: ")
        contador_intentos += 1
        superar_intentos = False
    else:
        superar_intentos = True

if superar_intentos:
    print("Lo siento, te quedaste sin intentos. El objeto era: Aguja.")
else:
    print("¡FELICITACIONES! ADIVINASTE EL OBJETO.")
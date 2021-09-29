import random
import sys 

adivinanza = [("Soy alta y delgada, tengo un ojo, hago vestidos y no me los pongo. ¿Quién soy?", "Aguja"),
              ("Es larga y de lana, y cuando hace frío se la pone mi hermana. ¿Quién soy?", "Bufanda"), 
              ("Cuando llueve y sale el sol, todos los colores tengo yo. ¿Quién soy?", "Arcoiris"), 
              ("Soy astuto y juguetón y cazar un ratón es mi mayor afición. ¿Quién soy?", "Gato")]


intento = ""
contador_intentos = 0
max_intentos = 1
superar_intentos = False

try: 
    max_intentos = int(input("¿Cuántos intentos desea realizar?: "))
except:
    print("No es un valor numérico.")
    sys.exit()

adivinanza_tupla = random.choice(adivinanza)
print(adivinanza_tupla[0])

while intento != adivinanza_tupla[1] and not(superar_intentos):
    if contador_intentos < max_intentos:
        intento = input("Ingrese la palabra: ")
        contador_intentos += 1
        superar_intentos = False
    else:
        superar_intentos = True

if superar_intentos:
    print("Lo siento, te quedaste sin intentos. El objeto era " + adivinanza_tupla[1])
else:
    print("¡FELICITACIONES! ADIVINASTE EL OBJETO.")

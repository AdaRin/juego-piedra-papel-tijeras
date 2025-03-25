nombre1 = input("Cómo se llamará el jugador 1?: ")
nombre2 = input("Cómo se llamará el jugador 2?: ")

print("Hola ", nombre1 + " eres el juegador número 1")
jugador1 = input("Qué eliges? Piedra, papel o tijera?: ")
print("Hola ", nombre2 + " eres el juegador número 2")
jugador2 = input("Qué eliges? Piedra, papel o tijera?: ")


#Separamos las condiciones realizando Refactorización

condicion1 = jugador1=="piedra" and jugador2=="tijeras"
condicion2 = jugador1=="papel" and jugador2=="pidra"
condicion3 = jugador1=="tijeras" and jugador2=="papel"


if jugador1 == jugador2:
    print("Ha sido un empate")
elif condicion1 or condicion2 or condicion3:
    print("Ha ganado el jugador ", nombre1)
else:
        print("Ha ganado el jugador ", nombre2)


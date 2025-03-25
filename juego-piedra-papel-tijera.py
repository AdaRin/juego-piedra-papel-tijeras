nombre1 = input("Cómo se llamará el jugador 1?: ")
nombre2 = input("Cómo se llamará el jugador 2?: ")

print("Hola ", nombre1 + " eres el juegador número 1")
jugador1 = input("Qué eliges? Piedra, papel o tijera?: ")
print("Hola ", nombre2 + " eres el juegador número 1")
jugador2 = input("Qué eliges? Piedra, papel o tijera?: ")

if jugador1 == jugador2:
    print("Ha sido un empate")
elif (jugador1=="piedra" and jugador2=="tijeras") or (jugador1=="papel" and jugador2=="pidra") or (jugador1=="tijeras" and jugador2=="papel"):
    print("Ha ganado el jugador ", nombre1)
else:
        print("Ha ganado el jugador ", nombre2)

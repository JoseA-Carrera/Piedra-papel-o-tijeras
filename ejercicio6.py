'''
Ejercicio 6
hacer un piedra, papel o tijeras
'''
import random

op = ["piedra", "papel", "tijeras"]
sep = "-" * 15

while True:
    user = input("\nElije: piedra, papel o tijeras: ").lower()
    if user not in op:
        print("\nMovimiento no valido")
        continue
    pc = random.choice(op)
    print(f"\nLa pc ha seleccionado {pc}")

    if user == pc:
        print(f"Empate!, ambos utilizaron {user}")
    elif user == "piedra" and pc == "tijeras":
        print(f"\nGanaste!, {user} gana sobre {pc}")
    elif user == "papel" and pc == "piedra":
        print(f"\nGanaste!, {user} gana sobre {pc}")
    elif user == "tijeras" and pc == "papel":
        print(f"\nGanaste!, {user} gana sobre {pc}")
    else:
        print(f"\nPerdiste, {user} pierde sobre {pc}")

    print(f"\n{sep}FIN DE LA PARTIDA{sep}")

"""
    proyecto python y msql
    - abrir asistente
    - login o registro
    - si elegimos registro, creara un usuario en la bbdd
    - crear nota, mostrar nogtas, borrarlas
"""

print("""
Acciones disponibles:
    -registro
    -login
""")

action = input("Que quieres hacer?: ")

if action == "registro":
    print("\nok, Vamos a regustrarte en el sistema")
    name = input("Cual es tu nombre?: ")
    

if action == "login":
    print("vale, identificate en el sistema...")



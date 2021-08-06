"""
    proyecto python y msql
    - abrir asistente
    - login o registro
    - si elegimos registro, creara un usuario en la bbdd
    - crear nota, mostrar nogtas, borrarlas
"""
import users.actions as actions

make = actions.Actions

# this is a menu whith my proyect of python
print("""
Acciones disponibles:
    -registro
    -login
""")
# start the action question "whit do u want to do"
action = input("Que quieres hacer?: ")
# condicional, log up
if action == "registro":
    make.registrer()

# condicional, log in
if action == "login":
    make.login()
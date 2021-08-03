import usuario as model

class Actions:
    def registrer(self):

        print("\nok, Vamos a registrarte en el sistema")
        name = input("Cual es tu nombre?: ")
        surnames = input("Cuales son tus apellidos?: ")
        email = input("Cual es tu email? (no puede estar repetido): ")
        password = input("Introduce tu contraseña: ")

        data= model.Usuario(name, surnames, email, password)
        complete = data.registrar()

        if complete[0] >= 1:
            print(f"Perfecto {complete[1].name} te has registrado")
        else:
            print("no te has registrado ")

    def login(self):
        print("\n vale, identificate en el sistema...")
        email = input("Cual es tu email?: ")
        password = input("Introduce tu contraseña: ")
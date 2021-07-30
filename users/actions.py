class Actions:
    def registrer(self):

            print("\nok, Vamos a regustrarte en el sistema")
            name = input("Cual es tu nombre?: ")
            surnames = input("Cuales son tus apellidos?: ")
            email = input("Cual es tu email? (no puede estar repetido): ")
            password = input("Introduce tu contraseña: ")

    def login(self):
        print("vale, identificate en el sistema...")
        email = input("Cual es tu email?: ")
        password = input("Introduce tu contraseña: ")
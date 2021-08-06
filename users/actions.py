import users.usuario as model

class Actions:
    def registrer(self):

        print("\nok, Vamos a registrarte en el sistema")
        name = input("Cual es tu nombre?: ")
        surnames = input("Cuales son tus apellidos?: ")
        email = input("Cual es tu email? (no puede estar repetido): ")
        password = input("Introduce tu contrasinal: ")

        data= model.Usuario(name, surnames, email, password)
        complete = data.registrar()

        if complete[0] >= 1:
            print("Perfecto"+{complete[1].name} + "te has registrado ")
        else:
            print("no te has registrado ")

    def login(self):
        print("\n vale, identificate en el sistema...")

        try:
            email = input("Cual es tu email?: ")
            password = input("Introduce tu contrasinal: ")

            usuario = model.Usuario("", "", email, password)
            login = usuario.identificar()

            if email == login[3]:
                print("bienvenido")
                self.nextactions(login)

        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print("usuario incorrecto")

    def nextactions(self, user):

        print("""
            Acciones disponbles:
            -Crear nota (crear)
            -Mostrar tus notas (mostrar)
            -Eliminar nota (eliminar)
            -Salir (salir)
        """)
        accion = input("Que quieres hacer??")

        if accion == "crear":
            print("Vamos a crear")
            self.nextactions(user)

        elif accion == "mostrar":
            print("Vamos a mostrar")
            self.nextactions(user)

        elif accion == "eliminar":
            print("Vamos a eliminar")
            self.nextactions(user)

        elif accion == "salir":
            exit()


        return None

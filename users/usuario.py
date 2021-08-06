import users.connect as connect
import datetime
import hashlib

connect = connect.Conexion()
database = connect[0]
arrow = connect[1]

class Usuario:

    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password

    def registrar(self):
        # insert the values in db
        sql ="INSERT INTO usuarios VALUES(null,%s, %s, %s, %s, %s)"

        # Encript the pasword
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode("utf8"))

        fecha = datetime.datetime.now()
        usser = (self.name, self.surname, self.email, cifrado.hexdigest(), fecha)

        try:
            arrow.execute(sql, usser)
            database.commit()
            result = [arrow.rowcount, self]
        except:
            result = [0, self]

        return result

    def identificar(self):

        # check if user exist
        sql= "SELECT * FROM usuarios WHERE email = %s AND password = %s "

        # Encript the pasword
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode("utf8"))

        # data for the call
        user = (self.email,cifrado.hexdigest())

        arrow.execute(sql, user)
        result = arrow.fetchone()

        return result

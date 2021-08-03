import mysql.connector
import datetime
import hashlib

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="master_python",
    port="3306"
)

arrow = database.cursor(bufered=True)

class Usuario:

    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password

    def registrar(self):
        """insert the values in db """
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
        return self.nombre
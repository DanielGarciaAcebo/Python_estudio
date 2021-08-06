import mysql.connector as mysql

def Conexion():

    database = mysql.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="master_python",
        port="3306"
    )

    arrow = database.cursor(bufered=True)

    return [database, arrow]

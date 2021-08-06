import users.conect as conexion

class Note:

    def __init__(self,usuario_id, titulo, descripcion):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion

    def save(self):
        sql = "INSERT INTO notas VALUES (null, %n, %n, %n, now())"
        note = (self.usuario_id, self.titulo, self.descripcion)

        arrow.execute(sql, note)
        database.commit()
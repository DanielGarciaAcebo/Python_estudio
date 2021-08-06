import notes.note as modelo

class Acctions:

    def create(self, name):
        print("vamos a crear una nueva nota")
        titulo = input("introduze el titulo de la nota")
        descripcion = input("meteme el contenido de tu nota")

        note = modelo.Nota(usuario[0], titulo, descripcion)

        guardar= note.guardar()

        if guardar[0] >= 1:
            print("se ha guradado la nota ")

        else:
            print("no se ha guardado la not, lo siento")
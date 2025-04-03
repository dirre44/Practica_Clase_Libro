import unicodedata

class Libro:
    def __init__ (self, titulo, autor, genero, puntuacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.puntuacion = puntuacion

    def __str__(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Genero: {self.genero}, Puntuacion: {self.puntuacion}"

def normalizar_texto(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn').lower()
    
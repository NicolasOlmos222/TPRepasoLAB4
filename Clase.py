class Libro:
    def __init__(self, titulo, autor, editorial, genero, ubicacion, cantidad):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.genero = genero
        self.ubicacion = ubicacion
        self.cantidad = int(cantidad)
    
    def modificar(self, titulo, autor, editorial, genero, ubicacion, cantidad):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.genero = genero
        self.ubicacion = ubicacion
        self.cantidad = int(cantidad)

    def getTitulo(self):
        return self.titulo

    def getAutor(self):
        return self.autor

    def getEditorial(self):
        return self.editorial

    def getGenero(self):
        return self.genero

    def getUbicacion(self):
        return self.ubicacion

    def getCantidad(self):
        return self.cantidad

    def mostrar(self):
        return f"{self.titulo} | {self.autor} | {self.editorial} | {self.genero} | {self.ubicacion} | {self.cantidad}"
class Pelicula:

    def __init__(self,titulo,director,clasificacion,imdb,reparto,genero,sala):
        self.titulo = titulo
        self.director = director
        self.clasificacion = clasificacion
        self.imdb = imdb
        self.reparto = reparto
        self.genero = genero
        self.sala = sala
    
    def descripcion_pelicula(self):
        print("Título: {} \nDirector: {} \nClasificacion: {} \nRating (IMDB): {} \nReparto: {} \nGenero: {} \nSala: {}"
        .format(self.titulo,self.director,self.clasificacion,self.imdb,self.reparto,self.genero,self.sala)
            )
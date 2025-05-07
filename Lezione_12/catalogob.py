

class MovieCatalog:


    def __init__(self):
        self.setCatalog()


#metodo che imposta il valore dell'attributo self.catalog 
    def setCatalog(self) -> None:
        self.catalog:dict[str, list[str]] = {}

#metodo che ritorna il valore dell'attributo 
    def getCatalog(self) -> dict[str, list[str]]:
        return self.catalog
    

    def __str__(self):
        return f"La lista è {self.getCatalog()} "

#metodo che aggiunge una lista di film al catalogo 
    def add_movie(self, director_name:str, movies:list[str]) -> None:

        if not director_name:
            print("Fornire un nome valido per il regista")

        #check valore valido di movie 
        elif not movies:
            print("Fornire una lista di film che non sia vuota")

        #se i dati ineriti sono validi
        else: 

            #se il regista è presente nel catalogo, aggiungi i film 
            if director_name in self.catalog:
            #aggiungere film al catalogo 
                for movie in movies:
                #controlliamo se i film nella lista movie siano gia stati inseriti all'interno del catalogo  
                    if movie in self.catalog[director_name]:
                        #self.catalog[director_name] è la lista dei film prodotti dal regista 
                        #dove self.catalog è un dizionario
                        # director_name è la chiave
                        #self.catalog[director_name] è il valore corrispondente alla chiave
                        print(f"Il film {movie} è gia presente nel catalogo ")
                    else:
                        self.catalog[director_name].append(movie)

            # se il regista non è presente nel catalogo, creare un nuovo record che ha come chiave 
            else:
                self.catalog[director_name] = movies

    def remove_movie(self, director_name: str, movie: list[str]) -> None:
    
        if not director_name:
            print("Fornire un nome valido per il regista")

        #check valore valido di movie 
        elif not movie:
            print("Fornire una lista di film che non sia vuota")

        #se i dati ineriti sono validi
        else:
        
            if director_name in self.catalog and movie in self.catalog[director_name]:

            #rimuovi il film dalla lista 
                self.catalog[director_name].remove(movie)


        #se la lista dei film è vuota, rimuovere il regista dal catalogo 
            if not self.catalog[director_name]:

                del self.catalog[director_name] 
    
    def list_directors(self) -> list[str]:
        return list(self.catalog.keys())
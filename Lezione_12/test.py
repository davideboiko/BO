from catalogob import MovieCatalog


#creare un oggetto dalla classe MovieCatalog

catalog:MovieCatalog = MovieCatalog() 


catalog.add_movie("ER Pisda", ["PasholNaxui", "Suca"])

#aggiungi altro film di ER Pisda

catalog.add_movie("ER Pisda", ["SucaBlyat"]) 


catalog.add_movie("Stiopa", ["Casiol", "Dibil"])


catalog.remove_movie("ER Pisda", "Suca")

print(catalog.getCatalog())

print(catalog.getCatalog())


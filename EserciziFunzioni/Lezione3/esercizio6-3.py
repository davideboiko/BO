def glossary():

    glossary:dict = {"print()":"Stampa qualcosa a schermo",
                    "input()":"Legge un valore inserito dall'utente (come stringa)",
                    "len()":"Restituisce la lunghezza (numero di elementi) di una stringa, lista, o altro oggetto iterabile",
                    "range()":" Crea una sequenza di numeri. Spesso usato nei cicli for",
                    "if/elif/else":" Serve per prendere decisioni (controllo del flusso)"}
    
    for key, value in glossary.items():
        print(f"{key}:\n{value}\n")
    
glossary()
    

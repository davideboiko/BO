nome:str = input("Inserire nome:")
ruolo:str = input("Inserire ruolo:")
age:int = int(input("Inserire age:"))

match ruolo:
    case "Admin":
        print("Accesso completo a tutte le funzionalità")
    case "Moderatore":
        print("Può gestire i contenuti ma non modificare le impostazioni")
    case "Utente adulto":
        if age > 18:
            print("Accesso standard a tutti i servizi")
        else:
            print("Attenzione! Ruolo non riconsciuto! Accesso Negato!")
    case "Utente minorenne":
        if age < 18:
            print("Accesso limitato! Alcune funzionalità sono bloccate")
        else:
            print("Attenzione! Ruolo non riconsciuto! Accesso Negato!")
    case "Ospite":
        print("Accesso ristretto! Solo visualizzazione dei contenuti")
    case  _:
        print("Attenzione! Ruolo non riconsciuto! Accesso Negato!")


#utilizzo di un dizionario per inserire i dati


user:dir[str, str|int] = dict()

user["name"] = input("Inserire nome:")
user["ruolo"] = input("Inserire ruolo:")
user["age"] = int(input("Inserire età:"))

match user:
    case {"ruolo": "Admin"}:
    case {"ruolo": "Moderatore"}:
    case {"ruolo": "Utente Adulto"}:
    case {"ruolo": "Utente Minorenne"}:
    case {"ruolo": "Ospite"}:
    case _:





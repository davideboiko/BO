class ContactManager:
    def __init__(self, contacts: dict[str, list[str]] = {}):


        self.contacts = contacts


    def create_contact(self, name: str, phone_numbers: list[str]) -> dict[str, list[str]]:
      
        """creazione di un contatto """
      
        if not name in self.contacts:
           
            raise ValueError("Fornire un nome valido per il contatto.")
       
        else:

            self.contacts[name] = phone_numbers

        return {name: phone_numbers} 

    def add_phone_number(self, contact_name: str, phone_number: str) -> dict[str, list[str]]:
   
        """Aggiunge un numero di telefono a un contatto, creando il contatto se non esiste."""
     
        if contact_name not in self.contacts:

            raise ValueError("Il contatto non esiste")
        
        if phone_number in self.contacts[contact_name]:

            raise ValueError("Errore: il numer è gia associato al contatto")
    
        self.contacts[contact_name].append(phone_number)

        return {contact_name : self.contacts[contact_name]}

    def remove_phone_number(self, contact_name: str, phone_number: str) -> None:
        """Rimuove un numero di telefono da un contatto. Se il contatto rimane senza numeri, lo elimina."""
        if contact_name not in self.contacts:

            raise ValueError("Fornire un nome valido per il contatto.")
            

        if phone_number not in self.contacts[contact_name]:

            raise ValueError("Fornire un numero di telefono valido.")

        self.contacts[contact_name].remove(phone_number)

        return {contact_name : self.contacts[contact_name]}
        
    def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number: str) -> dict[str, list[str]]:

        if contact_name not in self.contacts:

            raise ValueError("Fornire un nome valido per il contatto.")
        
        if old_phone_number not in self.contacts[contact_name]:

            raise ValueError("Fornire un nome valido per il contatto.")
        
        index: int = self.contacts[contact_name].index(old_phone_number)

        self.contacts[contact_name][index] = new_phone_number

        return {contact_name : self.contacts[contact_name]}


    def list_contacts(self) -> list[str]:
        """Restituisce la lista dei nomi dei contatti."""
        return self.contacts.keys()
    
    def list_phone_numbers(self, contact_name: str)  -> list[str]: 

        if contact_name not in self.contacts:

            raise ValueError("Fornire un nome valido per il contatto.")

        return self.contacts[contact_name]

    def search_contact_by_phone_number(self, phone_number: str) -> list[str]:

        contacts_list: list[str]  = [] 

        for contacts, list_contacts in contacts_list.items():

            if phone_number in list_contacts:

                contacts_list.append(contacts)
            
            if contacts_list == []:

                raise Exception("Nessun contatto trovato con quesrto numero di telefono")
            
            return contacts_list




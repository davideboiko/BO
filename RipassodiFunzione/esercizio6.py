def create_contact(name: str, email: str = None, telefono: int = None) -> dict:
    return {
        'profile': name,
        'email': email,
        'telefono': telefono
    }

def update_contact(dictionary: dict, name: str, email: str = None, telefono: int = None) -> dict:
   
    if email is not None:
        dictionary['email'] = email
    if telefono is not None:
        dictionary['telefono'] = telefono

    return dictionary


contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787))
print(update_contact(contact, "Mario Rossi", telefono=123456789))

contact = create_contact("Laura Neri", email="laura.neri@domain.com")
print(create_contact("Laura Neri", email="laura.neri@domain.com"))
print(update_contact(contact, "Laura Neri", email="laura.new@domain.com", telefono=84736736))
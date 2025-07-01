from esercitazione import Email

email = Email(
    text="Ciao Bob, possiamo incontrarci domani?",
    mittente="alice@example.com",
    destinatario="bob@example.com",
    titolo_m="Incontro"
)

print(email.getText())
print(email.isInText("incontrarci"))   # True
print(email.isInText("riunione"))      # False

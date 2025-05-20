def checkingUser():
    current_users:list[str] = ["Alessandro", "Davide", "Popa",
                       "Alessio", "Marco", "admin"]
    new_users:list[str] = ["AlessAndRo", "a1", "a2",
                       "a3", "a4", "a5"]
    cunu:list[str] = [user.casefold() for user in current_users]
    for nu in new_users:
        if nu.casefold() in cunu:
            print(f"L'utente {nu} non può essere usato")
        else:
            print(f"L'utente {nu} può essere usato")

checkingUser()










"""""
esempio:

 for value in elements:
        if value in num:
            num[value] += 1
        else:
            num[value] = 1
    return num
"""""
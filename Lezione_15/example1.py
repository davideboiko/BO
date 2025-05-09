with open("Lezione_15/example1.txt", mode="w", encoding="utf-8") as file:
    message:str = "Hello World \n"
    written_char:int = file.write(message)
    print(f"Written characters: {written_char}")
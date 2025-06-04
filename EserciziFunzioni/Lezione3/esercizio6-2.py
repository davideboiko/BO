def favnum():

    person:dict = {"Andre":5, "Paolo":10,
                     "Camilla":20,"Davide":15, "Anna":0}
    
    for key, value in person.items():
        print(f"{key}:{value}")
    
favnum()
    

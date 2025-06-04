def person():

    person:dict = {"first_name":"Davide", "last_name":"Boyko",
                     "age":20,"city":"Roma"}
    
    for key, value in person.items():
        print(f"{key}:{value}")
    
person()
    

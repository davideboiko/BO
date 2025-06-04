def person2():

    bo:list[dict] = [{"first_name":"Davide", "last_name":"Boyko",
                     "age":20,"city":"Roma"},
                    {"first_name":"Marco", "last_name":"Tiritillo",
                     "age":25,"city":"Roma"},
                    {"first_name":"Francesco", "last_name":"Totti",
                     "age":50,"city":"Roma"}
                    ]
    
    for i in bo:
        for key, value in i.items():
            print(f"{key}:{value}")
        print("-------------------------------")
person2()
    

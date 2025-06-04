def pet():

    pet:list[dict] = [{"name":"a1", "kind":"a2",
                     "description":"a3"},
                    {"name":"b1", "kind":"b2",
                     "description":"b3"},
                    {"name":"c1", "kind":"c2",
                     "description":"c3"}
                    ]
    
    for i in pet:
        for key, value in i.items():
            print(f"{key}:{value}")
        print("-------------------------------")
pet()
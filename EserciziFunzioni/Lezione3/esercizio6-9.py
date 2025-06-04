def favplace():

    favorite_places:list[dict] = [{"name_guy1":"a1", "place":"a2",
                     "placee":"a3"},
                    {"name_guy2":"b1", "place":"b2",
                     "placee":"b3"},
                    {"name_guy3":"c1", "place":"c2",
                     "placee":"c3"}
                    ]
    
    for i in favorite_places:
        for key, value in i.items():
            print(f"{key}:{value}")
        print("-------------------------------")
favplace()
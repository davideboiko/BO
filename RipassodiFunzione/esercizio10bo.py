def rimbalzo():
    tempo = 0
    altezza = 0.0
    velocita = 100.0
    rimbalzi = 0

    while rimbalzi < 5:
        print(f"Tempo: {tempo} Altezza: {altezza}")

        altezza += velocita
        velocita -= 96

        tempo += 1

        if altezza < 0:
            print(f"Tempo: {tempo} Rimbalzo!")
            tempo += 1
            altezza *= -0.5
            velocita *= -0.5
            rimbalzi += 1

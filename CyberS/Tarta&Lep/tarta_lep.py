import random

def visualizza_pista(pos_tartaruga, pos_lepre):
    # Lunghezza della pista
    pista = []

    # Crea ogni riquadro
    for i in range(70):
        if i == pos_tartaruga and i == pos_lepre:
            pista.append(f"{i + 1}[OUCH!!!]")
        elif i == pos_tartaruga:
            pista.append(f"{i + 1}[T,_]")
        elif i == pos_lepre:
            pista.append(f"{i + 1}[H,_]")
        else:
            pista.append(f"{i + 1}[_,_]")


    print(pista)
    
def mossa_tartaruga(pos):
    i = random.randint(1, 10)
    if 1 <= i <= 5:
        pos += 3
    elif 6 <= i <= 7:
        pos -= 6
    else:
        pos += 1
    
    return max(0, min(pos, 70))

def mossa_lepre(pos):
    i = random.randint(1, 10)
    if 1 <= i <= 2:
        pass
    elif 3 <= i <= 4:
        pos += 9
    elif i == 5:
        pos -= 12
    elif 6 <= i <= 8:
        pos += 1
    else:
        pos -= 2
    
    return max(0, min(pos, 70))

def gara():
    print("BANG !!!!! AND THEY'RE OFF !!!!!\n")

    posizione_tartaruga = 0
    posizione_lepre = 0

    while posizione_tartaruga < 70 and posizione_lepre < 70:

        posizione_tartaruga = mossa_tartaruga(posizione_tartaruga)
        posizione_lepre = mossa_lepre(posizione_lepre)

        visualizza_pista(posizione_tartaruga, posizione_lepre)

        if posizione_tartaruga >= 70 and posizione_lepre >= 70:
            print("\nIT'S A TIE.")
            
        elif posizione_tartaruga >= 70:
            print("\nTORTOISE WINS! || VAY!!!")
            
        elif posizione_lepre >= 70:
            print("\nHARE WINS || YUCH!!!")
            
gara()

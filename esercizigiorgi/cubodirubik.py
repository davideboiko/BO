from colorama import init, Back, Style

# Inizializza colorama
init(autoreset=True)

# Mappa dei colori (sfondo colorato)
color_map = {
    'W': Back.WHITE,
    'R': Back.RED,
    'B': Back.BLUE,
    'G': Back.GREEN,
    'O': Back.MAGENTA,  # Orange non esiste, uso magenta
    'Y': Back.YELLOW
}

# Facce del cubo
white  = [['W'] * 3 for _ in range(3)]
green  = [['G'] * 3 for _ in range(3)]
red    = [['R'] * 3 for _ in range(3)]
blue   = [['B'] * 3 for _ in range(3)]
orange = [['O'] * 3 for _ in range(3)]
yellow = [['Y'] * 3 for _ in range(3)]

def draw_face(face):
    """Disegna una faccia 3x3 con bordi neri attorno ai quadratini"""
    lines = [""] * 3 * len(face)  # 3 righe per ogni riga della faccia

    for row_idx, row in enumerate(face):
        top_line = ""
        middle_line = ""
        bottom_line = ""

        for color in row:
            top_line += "+---+"
            middle_line += "|" + color_map[color] + "   " + Style.RESET_ALL + "|"
            bottom_line += "+---+"

        lines[row_idx * 3]     = top_line
        lines[row_idx * 3 + 1] = middle_line
        lines[row_idx * 3 + 2] = bottom_line

    return lines

def merge_faces(*faces):
    """Unisce le linee orizzontalmente (per le 4 facce centrali)"""
    face_lines = [draw_face(face) for face in faces]
    merged = []
    for i in range(len(face_lines[0])):
        merged.append("".join(face[i] for face in face_lines))
    return merged

# Stampa faccia sopra (white)
for line in draw_face(white):
    print(" " * 16 + line)

# Stampa facce centrali (green, red, blue, orange)
for line in merge_faces(green, red, blue, orange):
    print(line)

# Stampa faccia sotto (yellow)
for line in draw_face(yellow):
    print(" " * 16 + line)

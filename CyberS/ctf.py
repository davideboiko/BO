import math

# Funzione per calcolare l'inverso modulo
def mod_inv(a, m):
    return pow(a, m - 2, m)

# Funzione per calcolare il logaritmo discreto
def baby_step_giant_step(a, b, m):
    n = math.isqrt(m) + 1

    # Baby steps: calcoliamo a^j mod m
    baby_steps = {}
    current = 1
    for j in range(n):
        baby_steps[current] = j
        current = (current * a) % m

    # Calcoliamo a^(-n) mod m
    a_n_inv = mod_inv(pow(a, n, m), m)

    # Giant steps: calcoliamo i passi successivi
    current = b
    for i in range(n):
        if current in baby_steps:
            return i * n + baby_steps[current]
        current = (current * a_n_inv) % m

    return None  # Se non trovato

# Parametri del problema
a = 5  # Base
b = 26  # Risultato desiderato
m = 97  # Modulo

# Calcolo del logaritmo discreto
log_discreto = baby_step_giant_step(a, b, m)
print(f"Il logaritmo discreto di {b} in base {a} modulo {m} è: {log_discreto}")

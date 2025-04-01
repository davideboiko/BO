def calcola_media(numeri):
    """Calcola la media di una lista di numeri."""
    if len(numeri) == 0:
        return "La lista è vuota, impossibile calcolare la media."
    media = sum(numeri) / len(numeri)
    return media

class Frazione:
    def __init__(self, numeratore, denominatore):
        self.set_numeratore(numeratore)
        self.set_denominatore(denominatore)

    def set_numeratore(self, numeratore):
        if isinstance(numeratore, int):
            self.__numeratore = numeratore
        else:
            self.__numeratore = 13
            self.__denominatore = 5  # Fallback completo

    def set_denominatore(self, denominatore):
        if isinstance(denominatore, int) and denominatore != 0:
            self.__denominatore = denominatore
        else:
            self.__denominatore = 5

    def get_numeratore(self):
        return self.__numeratore

    def get_denominatore(self):
        return self.__denominatore

    def value(self):
        return round(self.__numeratore / self.__denominatore, 3)

    def __str__(self):
        return f"{self.__numeratore} / {self.__denominatore}"

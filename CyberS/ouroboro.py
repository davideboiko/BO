class FlagKeeper:
    def __init__(self):
        self.__secret_map = {
            'piece_0': "syntz", 
            'piece_1': "o", 
            'piece_2': "l|{qp",
            'piece_3': "gu@r",
            'piece_4': "=osr", 
            'piece_5': "fp\"g",
            'piece_6': ">\|{}" 
        }

    def __decode(self, text):
        return ''.join(chr(ord(c) - 13) for c in text)

    def get_flag(self):
        result = ""
        for i in range(7):
            part = self.__secret_map[f'piece_{i}']
            decoded_part = self.__decode(part)
            result += decoded_part
        return result

keeper = FlagKeeper()
print("FLAG trovata:", keeper.get_flag())

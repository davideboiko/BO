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
        self.__initialize()
    
    def __encode(self, text):
        return ''.join(chr(ord(c) + 13) for c in text)
    
    def __decode(self, text):
        return ''.join(chr(ord(c) - 13) for c in text)
    
    def __initialize(self):
        for i in range(7):
            method_name = f"__part_{i}"
            def make_method(index):
                def part(self):
                    return self.__secret_map[f'piece_{index}']
                return part
            setattr(FlagKeeper, method_name, make_method(i))
    
    def get_flag(self):
        result = ""
        for i in range(7):
            try:
                method_name = f"_FlagKeeper__part_{i}"
                method = getattr(self, method_name)
                result += method()
            except:
                result += "???"
        return result

keeper = FlagKeeper()
print("Output di get_flag():", keeper.get_flag())

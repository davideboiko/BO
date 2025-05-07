import math 
def memorizza_file(files: list[int]) -> None:
    spazio_totale_blocchi:int = 1000

    for i in files:
        if i < 512000:
            f_c = i * 0.8
            blocchi_tn: int = math.ceil(f_c / 512)
            blocchi_rm:int = spazio_totale_blocchi - blocchi_tn
            print(f"File di {i} byte compresso in {f_c} byte e memorizzato. Blocchi usati: {blocchi_tn}. Blocchi rimanenti: {blocchi_rm}.")
        else:
            print(f"Non è possibile memorizzare il file di {i} byte. Spazio insufficiente.")
            break
    
    return

	
memorizza_file([1100, 20000, 1048576, 512, 5000])














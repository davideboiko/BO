import subprocess
import re

def collega_nc():
    try:
        # Esegui il comando Netcat
        comando = ["nc", "2048.challs.olicyber.it", "10007"]
        processo = subprocess.Popen(comando, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


        while True:
            # Leggi l'output del server per estrarre l'operazione
            output = processo.stdout.readline().strip()
            if output == '':
                break

            print("Operazione ricevuta:", output)

            # Usa espressioni regolari per identificare e risolvere il tipo di operazione
            if "SOMMA" in output:
                numeri = list(map(int, re.findall(r'\d+', output)))
                risultato = str(sum(numeri))
            elif "DIVISIONE_INTERA" in output:
                numeri = list(map(int, re.findall(r'\d+', output)))
                risultato = str(numeri[0] // numeri[1])
            elif "DIFFERENZA" in output:
                numeri = list(map(int, re.findall(r'\d+', output)))
                risultato = str(numeri[0] - numeri[1])
            elif "PRODOTTO" in output:
                numeri = list(map(int, re.findall(r'\d+', output)))
                risultato = str(numeri[0] * numeri[1])
            else:
                risultato = '0'  # Fallback per eventuali altre operazioni
            
            # Invia il risultato al server
            print(f"Inviando risultato: {risultato}")
            processo.stdin.write(f"{risultato}\n")
            processo.stdin.flush()

        # Una volta terminato, chiudi il processo
        processo.stdin.close()
        processo.stdout.close()
        processo.stderr.close()

    except FileNotFoundError:
        print("Errore: Assicurati che Netcat (nc) sia installato sul tuo sistema.")
    except subprocess.TimeoutExpired:
        print("Errore: Timeout scaduto durante la connessione.")
    except Exception as e:
        print(f"Si è verificato un errore: {e}")

# Avvia la connessione e risolvi tutte le operazioni
collega_nc()

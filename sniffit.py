from scapy.all import sniff

def process_packet(packet):
    print(packet.summary())

def main():
    print("🛰️ Sniffit en cours... Appuyez sur Ctrl+C pour arrêter.\n")
    sniff(prn=process_packet, store=False)

if __name__ == "__main__":
    main()

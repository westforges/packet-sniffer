import socket
from parser import parse_ethernet_frame

def main():
    print("Starting educational packet monitor...")

    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    while True:
        raw_data, addr = conn.recvfrom(65535)
        dest_mac, src_mac, proto = parse_ethernet_frame(raw_data)
        print(f"\nSource: {src_mac} -> Destination: {dest_mac} | Protocol: {proto}")

if __name__ == "__main__":
    main()

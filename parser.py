import struct

def get_mac_addr(bytes_addr):
    return ':'.join(format(b, '02x') for b in bytes_addr)

def parse_ethernet_frame(data):
    dest, src, proto = struct.unpack('! 6s 6s H', data[:14])
    return get_mac_addr(dest), get_mac_addr(src), socket.htons(proto)

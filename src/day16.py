from utils import read_lines
from collections import namedtuple
import numpy as np

Packet = namedtuple('Packet', ['version', 'type_id', 'contents'])

hex_to_bin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}


def parse_literal(binary):
    i = 0
    result = ''
    while True:
        segment = binary[i:i+5]
        result += segment[1:]
        i += 5
        if segment.startswith('0'):
            break

    return int(result, 2), binary[i:]


def parse_packet(binary):
    version = int(binary[:3], 2)
    type_id = int(binary[3:6], 2)

    # literal
    if type_id == 4:
        literal, rest = parse_literal(binary[6:])
        return Packet(version, type_id, literal), rest

    length_type_id = int(binary[6:7], 2)
    if length_type_id == 0:
        content_bit_length = int(binary[7:22], 2)
        rest = binary[22:22+content_bit_length]
        sub_packets = []
        while len(rest) > 0:
            packet, rest = parse_packet(rest)
            sub_packets.append(packet)
        result = Packet(version, type_id, sub_packets)

        return result, binary[22+content_bit_length:]

    if length_type_id == 1:
        content_count = int(binary[7:18], 2)
        rest = binary[18:]
        sub_packets = []
        for _ in range(content_count):
            packet, rest = parse_packet(rest)
            sub_packets.append(packet)
        result = Packet(version, type_id, sub_packets)
        return result, rest


def version_sum(packet: Packet):
    if packet.type_id == 4:
        return packet.version

    return packet.version + sum(
        [version_sum(sub_packet) for sub_packet in packet.contents])


def execute(packet: Packet):
    type_id = packet.type_id

    if type_id == 4:
        return packet.contents

    sub_packets = [execute(sub) for sub in packet.contents]
    if type_id == 0:
        return sum(sub_packets)
    if type_id == 1:
        return np.product(sub_packets)
    if type_id == 2:
        return min(sub_packets)
    if type_id == 3:
        return max(sub_packets)
    if type_id == 5:
        return 1 if sub_packets[0] > sub_packets[1] else 0
    if type_id == 6:
        return 1 if sub_packets[0] < sub_packets[1] else 0
    if type_id == 7:
        return 1 if sub_packets[0] == sub_packets[1] else 0

    return None


def run1(data):
    binary = ''.join(list(map(lambda x: hex_to_bin[x], data)))
    root_packet, rest = parse_packet(binary)
    return version_sum(root_packet)


def run2(data):
    binary = ''.join(list(map(lambda x: hex_to_bin[x], data)))
    root_packet, rest = parse_packet(binary)
    return execute(root_packet)


if __name__ == '__main__':
    data = read_lines('inputs/day16.txt')
    print('[Part1]:', run1(data[0]))
    print('[Part2]:', run2(data[0]))

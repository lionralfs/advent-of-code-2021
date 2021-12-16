from utils import read_lines
from day16 import parse_packet, run1, run2
import pytest


def test_part1_full():
    data = read_lines('inputs/day16.txt')
    result = run1(data[0])
    assert result == 920


def test_part2_full():
    data = read_lines('inputs/day16.txt')
    result = run2(data[0])
    assert result == 10185143721112


def test_parse_packet1():
    result, rest = parse_packet('110100101111111000101000')
    assert rest == '000'
    assert result.version == 6
    assert result.type_id == 4
    assert result.contents == 2021


def test_parse_packet2():
    result, rest = parse_packet(
        '00111000000000000110111101000101001010010001001000000000')
    assert rest == '0000000'
    assert result.version == 1
    assert result.type_id == 6
    assert len(result.contents) == 2


def test_parse_packet3():
    result, rest = parse_packet(
        '11101110000000001101010000001100100000100011000001100000')
    assert rest == '00000'
    assert result.version == 7
    assert result.type_id == 3
    assert len(result.contents) == 3


def test_version_sum1():
    assert run1('8A004A801A8002F478') == 16


def test_version_sum2():
    assert run1('620080001611562C8802118E34') == 12


def test_version_sum3():
    assert run1('C0015000016115A2E0802F182340') == 23


def test_version_sum4():
    assert run1('A0016C880162017C3686B18A3D4780') == 31


def test_execute1():
    assert run2('C200B40A82') == 3


def test_execute2():
    assert run2('04005AC33890') == 54


def test_execute3():
    assert run2('880086C3E88112') == 7


def test_execute4():
    assert run2('CE00C43D881120') == 9


def test_execute5():
    assert run2('D8005AC2A8F0') == 1


def test_execute6():
    assert run2('F600BC2D8F') == 0


def test_execute7():
    assert run2('9C005AC2F8F0') == 0


def test_execute8():
    assert run2('9C0141080250320F1802104A08') == 1


if __name__ == '__main__':
    pytest.main(args=['-s'])

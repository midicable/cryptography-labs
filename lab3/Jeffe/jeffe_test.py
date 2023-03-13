from Jeffe.jeffe import JEFFE
from LFSR.lfsr import LFSR


def tau(x):
    return (-1)**x


def test_jeffe(N):
    lfsr1 = LFSR('00010', '01111')
    lfsr2 = LFSR('1100101', '0101111')
    lfsr3 = LFSR('00000001', '10011101')
    jeffe_generator = JEFFE(lfsr1, lfsr2, lfsr3)

    jeffe_sequence = jeffe_generator.generate_sequence(N)
    jeffe_sequence_zeros_count = jeffe_sequence.count('0')
    jeffe_sequence_ones_count = jeffe_sequence.count('1')

    r = list()
    for i in range(1, 6):
        total = 0
        for j in range(N - i):
            total += tau(int(jeffe_sequence[j]) ^ int(jeffe_sequence[j + i]))
        r.append(total)

    print(f'Jeffe sequence: {jeffe_sequence}')
    print(f'Zeros: {jeffe_sequence_zeros_count}')
    print(f'Ones: {jeffe_sequence_ones_count}')
    for i in range(len(r)):
        print(f'r[{i + 1}]: {r[i]}', end=', ')
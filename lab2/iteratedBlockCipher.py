def generate_round_key(key_init, bit_number_sequence):
    round_key = ''
    for bit_number in bit_number_sequence:
        round_key += key_init[bit_number - 1]

    return round_key


def substitution_block_1(bit_sequence):
    substitution_table = {
        '0000': '1110', '0001': '0100', '0010': '0110', '0011': '0010',
        '0100': '1011', '0101': '0011', '0110': '1101', '0111': '1000',
        '1000': '1100', '1001': '1111', '1010': '0101', '1011': '1010',
        '1100': '0000', '1101': '0111', '1110': '0001', '1111': '1001',
    }
    return substitution_table[bit_sequence]


def substitution_block_2(bit_sequence):
    substitution_table = {
        '0000': '0011', '0001': '0111', '0010': '1110', '0011': '1001',
        '0100': '1000', '0101': '1010', '0110': '1111', '0111': '0000',
        '1000': '0101', '1001': '0010', '1010': '0110', '1011': '1100',
        '1100': '1011', '1101': '0100', '1110': '1101', '1111': '0001',
    }
    return substitution_table[bit_sequence]


def permutation_block(bit_sequence):
    permutation = [4, 3, 2, 1, 6, 5, 8, 7]
    permuted_bit_sequence = ''
    for bit_number in permutation:
        permuted_bit_sequence += bit_sequence[bit_number - 1]

    return permuted_bit_sequence


def SP_substitution(X, key_init, bit_number_sequences):
    for bit_number_sequence in bit_number_sequences:
        round_key = generate_round_key(key_init, bit_number_sequence)
        T = format(int(X, 2) ^ int(round_key, 2), '#010b')[2:]
        T1, T2 = T[0:4], T[4:]
        N1, N2 = substitution_block_1(T1), substitution_block_2(T2)
        N = N1 + N2
        P = permutation_block(N)
        X = P

    return X
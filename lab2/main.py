from iteratedBlockCipher import SP_substitution


def main():
    bit_number_sequences = [[1, 4, 7, 10, 2, 5, 8, 11],
                            [2, 5, 8, 11, 3, 6, 9, 12],
                            [3, 6, 9, 12, 10, 4, 7, 1]]
    key_init             = '110111110000'
    X                    = '00100011'
    Y = SP_substitution(X, key_init, bit_number_sequences)

    print(f'X (input): {X}')
    print(f'Y (output): {Y}')


if __name__ == '__main__':
    main()
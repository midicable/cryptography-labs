from ciphers import substitution_cipher, vigenere_decipher


def main():
    print(f'Шифрование простой замены: {substitution_cipher("конфиденциальность")}')
    print(f'Дешифрация шифра Виженера: {vigenere_decipher("ЛИКШЙПЛ", "ЛБВ")}')


if __name__ == '__main__':
    main()


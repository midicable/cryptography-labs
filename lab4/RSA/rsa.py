def extended_euclid_algorithm(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_euclid_algorithm(b, a % b)
        return d, y, x - y * (a // b)


def generate_private_key(p, q):
    n = p * q                           # модуль
    phi = (p - 1) * (q - 1)             # функция Эйлера от n
    e = 110066171603901969362593059313  # открытая экспонента (уже дана в варианте лабораторной)
    _, d, _ = extended_euclid_algorithm(e, phi)

    return d, n


def cipher(plain_text, e, n):
    return pow(plain_text, e, n)


def decipher(ciphered_text, d, n):
    return pow(ciphered_text, d, n)
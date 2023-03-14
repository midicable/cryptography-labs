from RSA.rsa import generate_private_key, cipher, decipher


def test_rsa(p, q, e, X1, Y2):
    d, n = generate_private_key(p, q)

    Y1 = cipher(X1, e, n)
    Y1_deciphered = decipher(Y1, d, n)
    X2 = decipher(Y2, d, n)

    print(f'X1: {X1}, Y1: {Y1}, Y1 deciphered: {Y1_deciphered}')
    print(f'Y2: {Y2}, X2: {X2}')
import math
from random import randrange
from hashlib import sha256
from additionalAlgorithms import extended_euclid_algorithm, generate_R


def generate_keys(q):
    R = generate_R(q)
    while True:
        x = randrange(2, q)
        g = pow(x, R, q)
        if g != 1:
            break
    y = pow(g, x, q)

    return y, g, x


def sign(q, g, x, message):
    m = int(sha256(message.encode('utf-8')).hexdigest(), 16)
    while True:
        k = randrange(2, q)
        if math.gcd(k, q - 1) == 1:
            break
    r = pow(g, k, q)
    _, k_inversed, _ = extended_euclid_algorithm(k, q - 1)
    s = ( k_inversed * ( (m - x * r) % (q - 1) ) ) % (q - 1)

    return r, s


def verify(q, g, y, message, r, s):
    if not (r in range(1, q) and s in range(1, q - 1)):
        return False
    m = int(sha256(message.encode('utf-8')).hexdigest(), 16)
    if (pow(y, r, q) * pow(r, s, q)) % q == pow(g, m, q):
        return True
    else:
        return False







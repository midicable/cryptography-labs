# primitive root for prime numbers
def generate_R(q):
    R = 4 * (q + 1) - 1
    if R % 2 == 0:
        return R
    else:
        return R - 1


def extended_euclid_algorithm(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_euclid_algorithm(b, a % b)
        return d, y, x - y * (a // b)
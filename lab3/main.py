from LFSR.lfsr_test import test_lfsr
from Jeffe.jeffe_test import test_jeffe


def main():
    test_lfsr('00010', '01111')
    test_lfsr('1100101', '0101111')
    test_lfsr('00000001', '10011101')
    test_jeffe(10000)


if __name__ == '__main__':
    main()
class JEFFE:
    def __init__(self, lfsr1, lfsr2, lfsr3):
        self.lfsr1 = lfsr1
        self.lfsr2 = lfsr2
        self.lfsr3 = lfsr3

    def generate_sequence(self, N):
        generated_sequence = ''
        for _ in range(N):
            s1 = int(self.lfsr1.change_state()) # t-ый элемент выходной последовательности РСЛОС 1
            s2 = int(self.lfsr2.change_state()) # t-ый элемент выходной последовательности РСЛОС 2
            s3 = int(self.lfsr3.change_state()) # t-ый элемент выходной последовательности РСЛОС 3
            gamma = (s1 * s2) ^ ((s1 ^ 1) * s3)
            generated_sequence += str(gamma)

        return generated_sequence



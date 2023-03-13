class LFSR:
    def __init__(self, initial_state, linear_feedback):
        self.state = list(initial_state)
        self.linear_feedback = list(linear_feedback)
        self.length = len(initial_state)

    def change_state(self):
        output_bit = self.state[-1]            # выходной бит, составляющий случайную битовую последовательность

        linear_feedback_bit = 0
        for i in range(self.length):
            linear_feedback_bit ^= int(self.state[i]) * int(self.linear_feedback[i])
        for i in range(self.length - 1, 0, -1):
            self.state[i] = self.state[i - 1]
        self.state[0] = str(linear_feedback_bit)

        return str(output_bit)


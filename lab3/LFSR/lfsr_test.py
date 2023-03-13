from LFSR.lfsr import LFSR


def test_lfsr(initial_state, linear_feedback):
    lfsr = LFSR(initial_state, linear_feedback)
    output_bit_sequence = ''
    lfsr_period = 0

    print('State:', ''.join(lfsr.state), end=', ')
    output_bit = lfsr.change_state()
    output_bit_sequence += output_bit
    lfsr_period += 1
    print('Output:', output_bit)

    while ''.join(lfsr.state) != initial_state:
        print('State:', ''.join(lfsr.state), end=', ')
        output_bit = lfsr.change_state()
        output_bit_sequence += output_bit
        lfsr_period += 1
        print('Output:', output_bit)

    print('State:', ''.join(lfsr.state), ', RETURNED TO INITIAL STATE')
    print()
    print('Output bit sequence:', output_bit_sequence)
    print('LFSR period:', lfsr_period)
    print('-------------------------------')

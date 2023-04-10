from algorithms import generate_keys, sign, verify


def main():
    q = 225523118922100465769758148413025421807220956799975071969675156327098020673011
    y, g, x = 0, 0, 0
    r, s = 0, 0
    message = 'I, Vysotski Bogdan, love MiKOZI'

    while True:
        option = int(input(f'1. Generate\n'
                           f'2. Sign\n'
                           f'3. Verify\n'
                           f'4. Exit\n'))

        if option == 1:
            y, g, x = generate_keys(q)
            print(f'y: {y}\n'
                  f'g: {g}\n'
                  f'q: {q}\n'
                  f'x: {x}\n')

        elif option == 2:
            r, s = sign(q, g, x, message)
            print(f'r: {r}\n'
                  f's: {s}\n')

        elif option == 3:
            isCorrect = verify(q, g, y, message, r, s)
            print(f'isCorrect = {isCorrect}\n')

        elif option == 4:
            break

        else:
            print('Error: incorrect input! Choose the right option.\n')

    return 0


if __name__ == '__main__':
    main()
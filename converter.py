import argparse


def main():
    parser = argparse.ArgumentParser(description='Pre-boot Manuscript CLI version ')
    parser.add_argument('-bin', '--binary', type=str, action='store', help='Binary')
    parser.add_argument('-dec', '--decimal', type=str, action='store', help='Decimal')
    parser.add_argument('-hex', '--hexadecimal', type=int, action='store', help='Hexadecimal')
    parser.add_argument('-oct', '--octal', type=str, action='store', help='Octal')
    args = parser.parse_args()

    print('--------------------------------------')
    print('*** BIN/DEC/HEX/OCT CONVERTER TOOL ***')
    print('--------------------------------------')
    print('Please select a datatype:')
    print('\n1. Binary')
    print('2. Decimal')
    print('3. Hexadecimal')
    print('4. Octal\n')

    datatype = input()
    if datatype.isdigit():
        datatype = int(datatype)

    while datatype not in range(1, 5):
        print("Please select a datatype by entering a number between 1 and 4.")
        datatype = input()
        if datatype.isdigit():
            datatype = int(datatype)

    if datatype is 1:
        print('Enter a binary value: (8 digits)')
        datainp = input()
        convert(datatype, datainp)

    elif datatype is 2:
        print('Enter a decimal value:')
        datainp = input()
        convert(datatype, datainp)

    elif datatype is 3:
        print('Enter a hexadecimal value:')
        datainp = input()
        convert(datatype, datainp)

    elif datatype is 4:
        print('Enter a octal value:')
        datainp = input()
        convert(datatype, datainp)


def convert(type, input):
    # Binary
    if type == 1:
        print('Binary:', input)
        binary = [128, 64, 32, 16, 8, 4, 2, 1]

        dec = 0
        for index, bit in enumerate(input):
            if int(bit) is 1:
                dec += binary[index]
        print('Decimal:', dec)





    # Decimal
    elif type == 2:
        print()

    # Hexadecimal
    elif type == 3:
        print()

    # Octal
    elif type == 4:
        print()


if __name__ == "__main__":
    main()

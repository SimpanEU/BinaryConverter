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
        convertToDecimal(datatype, datainp)

    elif datatype is 2:
        print('Enter a decimal value:')
        datainp = input()
        convertToDecimal(datatype, datainp)

    elif datatype is 3:
        print('Enter a hexadecimal value:')
        datainp = input()
        convertToDecimal(datatype, datainp)

    elif datatype is 4:
        print('Enter a octal value:')
        datainp = input()
        convertToDecimal(datatype, datainp)


def convertToDecimal(datatype, datainput):
    dec = 0

    if datatype == 1: # Binary
        binary = [128, 64, 32, 16, 8, 4, 2, 1]
        dec = 0
        for index, bit in enumerate(datainput):
            if int(bit) is 1:
                dec += binary[index]

    elif datatype == 2: # Decimal
        dec = datainput

    elif datatype == 3: # Hexadecimal
        A, B, C, D, E, F = 10, 11, 12, 13, 14, 15
        #datainput = datainput.split(2)

        print(datainput)

    elif datatype == 4: # Octal
        print()

    print('Decimal:', dec)

if __name__ == "__main__":
    main()

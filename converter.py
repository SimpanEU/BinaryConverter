import argparse


def main():
    parser = argparse.ArgumentParser(description='Binary/Decimal/Hex/Octal converting tool by Simpan.')
    parser.add_argument('-bin', '--binary', type=str, action='store', help='Binary')
    parser.add_argument('-dec', '--decimal', type=str, action='store', help='Decimal')
    parser.add_argument('-hex', '--hexadecimal', type=int, action='store', help='Hexadecimal')
    parser.add_argument('-oct', '--octal', type=str, action='store', help='Octal')
    args = parser.parse_args()

    print('Select the datatype you wish to convert (1-4):')
    print('\n1. Binary')
    print('2. Decimal')
    print('3. Hexadecimal')
    print('4. Octal\n')

    datatype = input()
    if datatype.isdigit():
        datatype = int(datatype)

    while datatype not in range(1, 5):
        print("Select a datatype by entering a number between 1 and 4.")
        datatype = input()
        if datatype.isdigit():
            datatype = int(datatype)

    print('Enter a value:')
    datainput = input()

    if datatype is 1:
        datatype = 'Binary'
        print(datatype+':', datainput)
        print('Decimal:', convert_to_decimal(datatype, datainput))
        print('Hex:', convert_to_hex(convert_to_decimal(datatype, datainput)).replace("0x", ""))
        print('Octal:', convert_to_oct(convert_to_decimal(datatype, datainput)).replace("0o", ""))

    elif datatype is 2:
        datatype = 'Decimal'
        print('Binary:', convert_to_binary(int(datainput)).replace("0b", ""))
        print(datatype + ':', datainput)
        print('Hex:', convert_to_hex(int(datainput)).replace("0x", ""))
        print('Octal:', convert_to_oct(int(datainput)).replace("0o", ""))

    elif datatype is 3:
        datatype = 'Hexadecimal'
        print('Binary:', convert_to_binary(convert_to_decimal(datatype, datainput)).replace("0b", ""))
        print('Decimal:', convert_to_decimal(datatype, datainput))
        print(datatype + ':', datainput)
        print('Octal:', convert_to_oct(convert_to_decimal(datatype, datainput)).replace("0o", ""))

    elif datatype is 4:
        datatype = 'Octal'
        print('Binary:', convert_to_binary(convert_to_decimal(datatype, datainput)).replace("0b", ""))
        print('Decimal:', convert_to_decimal(datatype, datainput))
        print('Hex:', convert_to_hex(convert_to_decimal(datatype, datainput)).replace("0x", ""))
        print(datatype + ':', datainput)


def convert_to_decimal(datatype, datainput):
    dec = 0
    if datatype == 'Binary':
        binary = [128, 64, 32, 16, 8, 4, 2, 1]
        for index, bit in enumerate(datainput):
            if int(bit) is 1:
                dec += binary[index]
    elif datatype == 'Hexadecimal':
        datainput = '0x' + datainput
        dec = int(datainput, 16)
    elif datatype == 'Octal':
        dec = int(datainput, 8)
    return dec


def convert_to_binary(datainput):
    binary = bin(datainput)
    return binary


def convert_to_oct(datainput):
    octal = oct(datainput)
    return octal


def convert_to_hex(datainput):
    hexadecimal = hex(datainput)
    return hexadecimal


if __name__ == "__main__":
    main()

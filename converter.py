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

    if datatype is 1:
        print('Enter a binary value:')
        bin = input()
    elif datatype is 2:
        print('Enter a decimal value:')
        dec = input()
    elif datatype is 3:
        print('Enter a hexadecimal value:')
        hex = input()
    elif datatype is 4:
        print('Enter a octal value:')
        oct = input()



if __name__ == "__main__":
    main()

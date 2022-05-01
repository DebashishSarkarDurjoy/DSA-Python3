keypad = ["", "", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

def smartKeypad(input, output, i):
    # base case
    if (len(input) == i):
        print(output)
        return

    # recursive case
    current_digit = int(input[i])
    if (current_digit == 0 or current_digit == 1):
        smartKeypad(input, output, i+1)

    for k in range(0, len(keypad[current_digit])):
        smartKeypad(input, output + keypad[current_digit][k], i+1)

    return

def main():
    num = input("Number: ")
    output = ""

    smartKeypad(num, output, 0)

if __name__ == "__main__":
    main()

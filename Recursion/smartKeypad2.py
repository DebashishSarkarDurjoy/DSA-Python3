keypad = ["", "", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

def smartKeypad(inputValue, output, i):
    if (i == len(inputValue)):
        print(output)
        return

    current_digit = int(inputValue[i])
    if (current_digit == 0 or current_digit == 1):
        smartKeypad(inputValue, output, i+1)

    for k in range(0, len(keypad[current_digit])):
        smartKeypad(inputValue, output + keypad[current_digit][k], i+1)


def main():
    inputValue = ""
    inputValue = input("Enter number: ")
    output = ""

    smartKeypad(inputValue, output, 0)






if __name__ == "__main__":
    main()

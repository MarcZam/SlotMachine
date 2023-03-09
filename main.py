MAX_LINES = 3

def deposit():
    while True:
        amount = input("What is your deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Invalid betting amount")
        else:
            print("Please enter a Number")

    return amount
                  
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) +")")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Invalid number of lines")
        else:
            print("Please enter a Number")

    return lines
def main():
    balance = deposit()
    lines = get_number_of_lines()

    print(balance, lines)

main()
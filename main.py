MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def deposit():
    while True:
        amount = input("What would you like to deposit? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number for deposit.")


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 < lines <= MAX_LINES:
                return lines
            else:
                print("Enter a valid number for lines.")
        else:
            print("Please enter a number for lines.")
    
def get_bet():
    while True:
        bet = input("How much you like to bet? $ ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET
                return bet
            else:
                print("Bet must between {MIN_BET} and {MAX_BET} .")
        else:
            print("Please enter a number for deposit.")

def main():
    balance  = deposit()
    lines = get_number_of_lines()
    print(balance, lines)


if __name__ == "__main__":
    main()
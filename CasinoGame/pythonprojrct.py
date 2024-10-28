from playsound import playsound
import random
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "\U0001F600": 2,"\U0001F48E": 4,"\U0001F62D": 6,"\U00002620": 8
}
symbol_value = {
    "\U0001F600": 5,"\U0001F48E": 4,"\U0001F62D": 3,"\U00002620": 2,
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    print()
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end="  |  ")
            else:
                print(column[row], end="  ")

        print()


def deposit():
    while True:
        print("\U0001F48E"*40)
        print("\U0001F48E                                                                            \U0001F48E")
        print("\U0001F48E                    Welcome to MAAS CASINO                                  \U0001F48E")
        print("\U0001F48E                                                                            \U0001F48E")
        print("\U0001F48E"*40)
        print()
        print("                    \U0001F525 Make your day with our slot machine\U0001F525                                      ")
        print("      \U0001F4B5 Have your capital ready for playing most successful slot in the town\U0001F4B5                  ")
        print("            \U0001F4A5 Get ready for the most awaiting game you ever played \U0001F4A5                            ")
        print("                \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0 \U0001F4B0......................................")
        print()
        print("start your game with deposit which helps you to participate in game \U0001F60E")
        amount = input("What would you like to deposit\U0001F4B5 : ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount


def get_number_of_lines():
    while True:
        print("|Here our slot machine is three-model and maximum number of lines that can be achived are 3..so go with the lines and try your luck|")
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:
        print()
        print("\U0001F61C Enter the bet wisely..so that you dont loose your deposit\U0001F61C")
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    playsound(r'C:\Users\hp\Downloads\sound.wav')
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    print()
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print("\U0001F911 \U0001F911 \U0001F911 \U0001F911 \U0001F911 \U0001F911 \U0001F911")
        print(f"Current balance is ${balance}")
        print()
        answer = input("Enter any ley to continue the game..\U0001F4B0..otherwise 'quit' to exit \U0001F6D1 the game:")
        print()
        if answer == "quit":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main()
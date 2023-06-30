import random

MIN_LINES = 1
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100
password = []

COLS = 3
ROWS = 3

symbol_count = {
    "A": 10,
    "B": 3,
    "C": 3,
    "D": 3,
}

symbol_value = {
    "A ": 5,
    "B": 4,
    "C": 3,
    "D": 2
}




def deposit():
    while True:
        balance = input('Enter your Deposit ')
        if balance.isdigit():
            balance = int(balance)
            if balance > 0:
                break
            else:
                print('Amount must be greater than zero')

        else:
            print('Enter a valid amount')

    return balance


def get_lines():
    while True:

        lines = input(f'How many lines do u want to bet {1} - {MAX_LINES} ? ')

        if lines.isdigit():
            lines = int(lines)
            if lines < MIN_LINES or lines > MAX_LINES:
                print(f'You can only bet from {MIN_LINES} to {MAX_LINES} lines')
            else:
                break
        else:
            print('Enter a valid number of lines')

    return lines


def get_bet():
    while True:
        amount = input('Enter your bet')
        if amount.isdigit():
            amount = int(amount)
            if amount < MIN_BET or amount > MAX_BET:
                print(f'Amount must be between {MIN_BET} $ - {MAX_BET}')
            else:
                break

        else:
            print('Enter a valid amount')

    return amount


def slot_machine(rows, cols, symbols):
    all_symbols = []
    for key, value in symbol_count.items():
        for _ in range(value):
            all_symbols.append(key)

    rows_ = []

    for _ in range(rows):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(cols):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        rows_.append(column)

    return rows_


def print_slot_machine(rows):
    for _ in rows:
        for i, row in enumerate(_):
            if i != len(_) - 1:
                print(row, end=" | ")
            else:
                print(row, end="")
        print()


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


def spin(balance):
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print('Insufficient funds')
        else:
            break

    print(f'You have placed {bet} $ bet on {lines} lines. Total bet {total_bet} $')

    start = input("Press Enter To Start The Game")
    if start != "":
           exit()
    rows = slot_machine(ROWS, COLS, symbol_count)
    print_slot_machine(rows)
    winnings, winning_lines = check_winnings(rows, lines, bet, symbol_value)
    print(f'You won {winnings} $')
    print(f'You won on lines:  {winning_lines} ')
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f'Current Balance is {balance}')
        answer = input("Press enter to spin or q to quit.")
        if answer == "q":
            break
        balance += spin(balance)
    print(f'You left with {balance}')


main()

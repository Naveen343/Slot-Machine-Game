import random

MAX_LINES = 3
MIN_AMOUNT = 1
MAX_AMOUNT = 100

ROWS = 3
COLS = 3

items_and_count = {
    'APPLES': 2,
    'ORANGE': 3,
    'MANGOS' : 4,
    'GRAPES': 5
}
items_and_values = {
    'APPLES': 4,
    'ORANGE': 3,
    'MANGOS' : 2,
    'GRAPES': 1
}

def winning(symbol_columns, lines, bet, values):
    winnings = 0
    line_that_won = []
    for line in range(lines):
        symbol = symbol_columns[0][line]
        for column in symbol_columns:
            symbol_tocheck = column[line]
            if symbol !=symbol_tocheck:
                break
        else:
            winnings += values[symbol] * bet
            line_that_won.append(line + 1)
        
    return winnings, line_that_won


def slot_machine_spin(rows,cols,items):
    all_symbols = []
    for item, items_count in items_and_count.items():
        for _ in range(items_count):
            all_symbols.append(item)

    symbol_columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            column.append(value)
            current_symbols.remove(value)
        
        symbol_columns.append(column)
    
    return symbol_columns
            
def print_slot_machine(symbol_columns):
    for row in range(len(symbol_columns[0])):
        for index, column in enumerate(symbol_columns):
            if index != len(symbol_columns)-1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:
        balance = input("Put your bet amount hommie : ")
        if balance.isdigit():
            balance = int(balance)
            if balance > 0:
                break
                # print(f"{balance} bucks")
            else:
                print("Bring up with some money !!!")
        else:
            print("That's not a proper bet amount ! Try again.")

    return balance

def get_number_of_lines():
    while True:
        lines = input("Now choose the number of lines to bet between (1-" +str(MAX_LINES)+ ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("choose a number between 1 and "+str(MAX_LINES)+" !")
        else:
            print("Enter a proper number.")

    return lines

def get_bet():
    while True:
        amount = input("How much would you put on each line ?")
        if amount.isdigit():
            amount = int(amount)
            if MIN_AMOUNT<= amount <= MAX_AMOUNT:
                break
            else:
                print(f"Go for an amount between ${MIN_AMOUNT} - ${MAX_AMOUNT}")
        else:
            print("Enter a proper amount.")

    return amount
def spin(balance):
    lines=(get_number_of_lines())
    while True:
        bet = get_bet()
        total_bet = lines * bet
        if total_bet > balance:
            print(f"You dont have enough balance, current balance is ${balance}. Lower your bet amount and try again")
        else:
            break
            
    print(f"You are betting {bet} on {lines} lines. Total bet will be : ${total_bet}")

    slots = slot_machine_spin(ROWS, COLS, items_and_count)
    print_slot_machine(slots)
    fetch_winnings, line_that_won = winning(slots, lines, bet, items_and_values)
    print(f"You won ${fetch_winnings}.")
    print(f"You won on lines:", *line_that_won)
    return fetch_winnings - total_bet
    
def main():
    total_amount = deposit()
    print(f"{total_amount} bucks")
    while True:
        print(f"current balance is ${total_amount}")
        user_inout = input("Press enter to play (q to quit). ")
        if user_inout == 'q':
            break
        total_amount += spin(total_amount)
    

main()

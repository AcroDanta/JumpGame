import keyboard
import time
import os


# Function to print the heads part
def print_heads(current_position):
    # List that contains the current strings to print the heads
    to_print = []

    # Appending strings to the list in correct order
    for num in current_position:
        if num < 5:
            to_print.append(' 0>')
        elif num == 5:
            to_print.append('   ')
        else:
            to_print.append('<0 ')

    # Printing the whole list of strings
    print('  '.join(map(str, to_print)))


# Function to print the arms part
def print_arms(current_position):
    # Variable used for aesthetic purposes
    backslash = "\\"

    # Due to problems with printing backslash in Python instead of creating a list of strings, We have to print the
    # whole row of arms string by string. The end variable determines how should the 'print' statement end,
    # by default it's /n, but we want to keep printing in the same row
    for num in current_position:
        if num < 5:
            print(" O", end=""), print(backslash, end="  ")
        elif num == 5:
            print("     ", end="")
        else:
            print("/O   ", end="")

    # Getting to new lane after loop
    print('')


# Function to print the arms part
def print_bellies(current_position):
    # List that contains the current strings to print the bellies
    to_print = []

    # Appending strings to the list in correct order
    for num in current_position:
        if num == 5:
            to_print.append('   ')
        else:
            to_print.append(' | ')

    # Printing the whole list of strings
    print('  '.join(map(str, to_print)))


# Function to print the legs part
def print_legs(current_position):
    # Variable used for aesthetic purposes
    backslash = "\\"

    # Due to problems with printing backslash in Python instead of creating a list of strings, We have to print the
    # whole row of legs string by string. The end variable determines how should the 'print' statement end,
    # by default it's /n, but we want to keep printing in the same row
    for num in current_position:
        if num == 5:
            print("     ", end="")
        else:
            print("/ ", end=""), print(backslash, end="  ")

    # Getting to new lane after the loop
    print('')


# Function to print the numbers, just to check if the program behaves as it should
def print_numbers(current_position):
    # List that contains the current strings to print the numbers
    to_print = []

    # To properly print the numbers (to make them match the body) we need to convert them to strings and add a space
    for num in current_position:
        to_print.append(' ' + str(num) + ' ')

    # Using the join and map function to properly print all numbers
    print('  '.join(map(str, current_position)))


# Function to print the whole body
# TO PRINT NUMBERS UNDER STICK-MANS UNCOMMENT THE FUNCTION
def print_full_body(current_position):
    print_heads(current_position)
    print_arms(current_position)
    print_bellies(current_position)
    print_legs(current_position)
    # print_numbers(current_position)


# Function to swap 2 positions in a list
def swap_positions(current_position, pos1, pos2):
    current_position[pos1], current_position[pos2] = current_position[pos2], current_position[pos1]

    return current_position


# Function to determine which stick-man can be moved to the right site
def move_to_right(current_position):
    current_position = list(current_position)

    # Scanning the list from right site to catch the first stick-man turned to the left side
    i = 10
    while i >= 0:
        # Checking if the current number is headed to right
        if current_position[i] < 5:
            try:
                # Checking if the next number is free to move
                if current_position[i + 1] == 5:
                    # Swapping the positions and breaking the loop
                    current_position = swap_positions(current_position, i, i + 1)
                    break
                # Checking if the second number after the found one is free to move
                elif current_position[i + 2] == 5:
                    # Swapping the positions and breaking the loop
                    current_position = swap_positions(current_position, i, i + 2)
                    break
                # If there is no possibility to move, the loop looks for another stick-man
                else:
                    i -= 1
            # Catching errors when moving stick-mans at the end of list
            except IndexError:
                pass
        # Moving to the next stick-man to the left site
        i -= 1

    return current_position


# Function to determine which stick-man can be moved to the left site
def move_to_left(current_position):
    current_position = list(current_position)

    # Scanning the list from left site to catch the first stick-man turned to the right side
    i = 0
    while i <= 10:
        # Checking if the current number is headed to left
        if current_position[i] > 5:
            try:
                # Checking if the next number is free to move
                if current_position[i - 1] == 5:
                    # Swapping the positions and breaking the loop
                    current_position = swap_positions(current_position, i, i - 1)
                    break
                elif current_position[i - 2] == 5:
                    # Swapping the positions and breaking the loop
                    current_position = swap_positions(current_position, i, i - 2)
                    break
                else:
                    # If there is no possibility to move, the loop looks for another stick-man
                    i += 1
            # Catching errors when moving stick-mans at the end of list
            except IndexError:
                pass
        # Moving to the next stick-man to the right site
        i += 1

    return current_position


# Function that checks if the game is won, returns False / True
def test_if_won(current_position):
    right_set = []
    left_set = []

    # Creating sets of first 5 numbers from both ends of the list
    # First 5 numbers from left site of list
    i = 0
    while i < 5:
        left_set.append(current_position[i])
        i += 1

    # First 5 numbers from right side
    i = -1
    while i > -6:
        right_set.append(current_position[i])
        i -= 1

    # Set of numbers, which should be on the right / left side of the string, if game is won
    correct_left_set = [6, 7, 8, 9, 10]
    correct_right_set = [0, 1, 2, 3, 4]

    # Variables which hold True / False
    # Depending on it if left/right_set has the same numbers as correct_left/right_set
    check_left = all(item in left_set for item in correct_left_set)
    check_right = all(item in right_set for item in correct_right_set)

    # Checking if both end contain the correct numbers, if yes the game is won
    if check_left and check_right:
        return True
    else:
        return False


# My hello declaration
def print_greetings():
    print("Welcome to my game!\n")
    print('The rules are very simple, in total there are 3 of them:')
    print('1. Stick-mans can only move to the site they are headed to.')
    print('2.Only one stick-man can move in one turn')
    print('3.There are 2 possible moves:')
    print('   A) You can move on the empty space ahead.')
    print('   B) You can jump over one person, if the person is headed to the opposite\n')
    print('To move use arrows on your keyboard, if you get stuck press "R"\n')

    print('Press anything to continue...')


def main():
    # The starting list for the game
    starting_position = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Assigning the starting position to another list, so we won't operate on it.
    current_position = starting_position
    # Variable that decides if the loop for the game should go on
    is_game_over = False

    # Printing the greeting, rules
    print_greetings()

    # Waiting for the player to press enter
    if keyboard.read_key() == '':
        pass

    os.system('cls')
    print_full_body(starting_position)
    # Using the sleep function so the stick-man won't move if the player pressed an arrow at the greeting screen
    time.sleep(0.2)

    # Loop for reading pushed keys
    while not is_game_over:
        # Checking if the "right" arrow has been pressed
        if keyboard.read_key() == 'right':
            current_position = move_to_right(current_position)
        # Checking if the "left" arrow has been pressed
        elif keyboard.read_key() == 'left':
            current_position = move_to_left(current_position)
        # Checking if the "r" key has been pressed
        elif keyboard.read_key() == 'r':
            current_position = starting_position

        # Checking if the game is finished after the last move
        is_game_over = test_if_won(current_position)
        os.system('cls')
        # Printing the current positions
        print_full_body(current_position)
        time.sleep(0.2)


main()

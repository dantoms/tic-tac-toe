from helpers import draw_board, check_turn, check_for_win
import os

spots = {1 : "1", 2 : "2", 3 : "3", 4 : "4", 5 : "5", 6 : "6", 7 : "7", 8 : "8", 9 : "9"}

playing = True
complete = False
turn = 0
prev_turn = -1

while playing:
    # clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)
    if prev_turn == turn:
        print("Invalid input. Please try again.")
    prev_turn = turn
    print(f"Player {str((turn % 2) + 1)} turn: Pick your spot or press 'q' to quit.")
    # ask user for their choice
    choice = input("Enter your choice (1-9): ")
    if choice == "q":
        playing = False
    # Check if choice is a number and is between 1 and 9
    elif choice.isdigit() and int(choice) in spots:
        # Check if choice is already taken
        if not spots[int(choice)] in {"X", "O"}:
            # Valid input, update the board and turn
            turn += 1
            spots[int(choice)] = check_turn(turn)
    if check_for_win(spots):
        playing, complete = False, True
    if turn > 8:
        playing = False

os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)
if complete:
    if check_turn(turn) == "X":
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
else:
    print("It's a draw!")

print("Thanks for playing!")
import random
def play():
    player = input("What's your choice? 'r' for Rock, 'p' for Paper, 's' for Scissors.\n")
    computer = random.choice(['r', 'p', 's'])

    print("You are " + player + " and " + "Opponent are " + computer + ".")
    print(player + "   Vs   " + computer)

    if player == computer:
        return 'It\'s a tie'

    if is_win(player, computer):
        return 'You won!'
    else:
        return 'You lost!'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

result = play()
print("Result ---> " + result)

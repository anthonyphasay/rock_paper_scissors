import random

def rock_paper_scissors_player(choice):
    rock = '''

    Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

    paper = '''
    
    Paper
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    '''

    scissors = '''

    Scissors
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    '''

    moves = [rock, paper, scissors]
    print(moves[choice])
    return choice

def rock_paper_scissors_computer():
    rock = '''

    Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

    paper = '''
    
    Paper
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    '''

    scissors = '''

    Scissors
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    '''

    moves = [rock, paper, scissors]
    random_moves_number = random.randint(0, 2)
    random_moves = str(moves[random_moves_number])

    print(random_moves)
    return random_moves_number


def game_rule():

    player = main()
    computer = rock_paper_scissors_computer()

    if player == 1 and computer == 0:
        return print("You win.")
    elif player == 0 and computer == 2:
        return print("You win.")
    elif player == 2 and computer == 1:
        return print("You win.")
    elif player == computer:
         return print("Draw.")
    else:
        return print("You lose!")


def main():

    choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

    return rock_paper_scissors_player(choose)

if __name__ == "__main__":
    game_rule()
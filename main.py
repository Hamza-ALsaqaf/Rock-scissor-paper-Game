import random

def get_player_choice():
    while True:
        choice = input("Enter your choice (Rock/Paper/Scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid choice. Please try again.")

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
        (player_choice == "paper" and computer_choice == "rock") or \
        (player_choice == "scissors" and computer_choice == "paper"):
        return "player"
    else:
        return "computer"

def play_game():
    player_score = 0
    computer_score = 0
    attempt_counter = 0

    while attempt_counter < 6:
        print("\nAttempt", attempt_counter + 1)
        player_choice = get_player_choice()
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        
        print("Player chooses:", player_choice)
        print("Computer chooses:", computer_choice)

        winner = determine_winner(player_choice, computer_choice)
        if winner == "player":
            print("Player wins the round!")
            player_score += 1
        elif winner == "computer":
            print("Computer wins the round!")
            computer_score += 1
        else:
            print("Round is a tie!")

        attempt_counter += 1

    print("\nGame Over!")
    print("Player Score:", player_score)
    print("Computer Score:", computer_score)

    if player_score > computer_score:
        print("Player wins the game!")
    elif player_score < computer_score:
        print("Computer wins the game!")
    else:
        print("Game ends in a tie!")

play_game()


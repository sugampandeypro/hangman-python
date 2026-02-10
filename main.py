import random

# Import the word list
from hangman_words import word_list

# Import hangman stages and logo
from hangman_art import stages, logo

# Total lives available
lives = 6

# Print the hangman logo at the start
print(logo)

# Choose a random word from the list
chosen_word = random.choice(word_list)

# Create placeholder for the word
placeholder = ""
word_length = len(chosen_word)

# Add underscores for each letter
for position in range(word_length):
    placeholder += "_"

# Display initial word state
print("Word to guess: " + placeholder)

# Game control flag
game_over = False

# Store correct guessed letters
correct_letters = []

# Store wrong guessed letters
wrong_letters = []

# Game loop
while not game_over:

    # Show remaining lives
    print(f"****************************{lives}/6 LIVES LEFT****************************")

    # Get user input
    guess = input("Guess a letter: ").lower()

    # Check if letter was already guessed
    if guess in correct_letters or guess in wrong_letters:
        print(f"You already guessed {guess}")
        continue

    display = ""

    # Build the word display
    for letter in chosen_word:
        if letter == guess:
            display += letter
            if guess not in correct_letters:
                correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    # Show updated word
    print("Word to guess: " + display)

    # Reduce life if guess is wrong
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        wrong_letters.append(guess)

        # End game if no lives left
        if lives == 0:
            game_over = True
            print(f"****************It was {chosen_word}! YOU LOSE****************")

    # End game if word is fully guessed
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # Display hangman stage
    print(stages[lives])

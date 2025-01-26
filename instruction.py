def main():
    word = select_word()
    guessed_letters = []
    incorrect_guesses = []
    remaining_attempts = 6
    game_over = False

    print("Welcome to Hangman!")
    print("Try to guess the word!")

    while not game_over:
        print("\nCurrent word: " + display_word(word, guessed_letters))
        display_attempts(remaining_attempts, incorrect_guesses)

        guess = get_user_guess(guessed_letters)
        guessed_letters, incorrect_guesses, remaining_attempts = update_game_state(word, guess, guessed_letters,
                                                                                   incorrect_guesses,
                                                                                   remaining_attempts)

        if check_win(word, guessed_letters):
            print(f"\nCongratulations! You've guessed the word: {word}")
            game_over = True
        elif check_game_over(remaining_attempts):
            print(f"\nGame Over! The word was: {word}")
            game_over = True

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == "y":
        main()


if __name__ == "__main__":
    main()


def select_word():
    import random
    f_words = open("words.txt", 'r')
    words = []
    for line in f_words:
        words.append(line) 
    f_words.close()
    word = random.choice(words)
    word= word[:-1]
    return word

def display_word(word, guessed_letter):
    text = list(len(word) * '_')  
    for i in range(len(word)):  
        for j in range(len(guessed_letter)):  
            if word[i] == guessed_letter[j]:  
                text[i] = guessed_letter[j] 
    return ''.join(text)

def  get_user_guess(guessed_letters) :
    a = str(input("Enter word \n"))
    while True :
        if len(a) != 1 or a in  guessed_letters :
            a=  str(input("Enter word again! \n"))
        else :
            guessed_letters.append(a)
            break
    return a

def update_game_state(word, guess, guessed_letters, remaining_attempts):
    if guess in word:
        print(f"The letter '{guess}' is correct!")
    else:
        print(f"The letter '{guess}' is incorrect!")
        remaining_attempts -= 1
    return guessed_letters, remaining_attempts

def check_win(word,guessed_letters) :
    l=0
    for i in range(len(word)) :
        for j in range (len(guessed_letters)) :
            if word[i] == guessed_letters[j] :
                l+= 1
    if len(word) == l :
        return True 
    else :
        return False
def   check_game_over(remaining_attempts) :
    if remaining_attempts > 0 :
        return False 
    else :
        return True
    
def display_attempts(remaining_attempts,guessed_letters) :
    print("Remaining attempts- ",remaining_attempts)
    print("Already typed: ", guessed_letters)


#main
def main():
    word = select_word()
    guessed_letters = []
    remaining_attempts = 6
    game_over = False

    print("Welcome to Hangman!")
    print("Try to guess the word!")

    while not game_over:
        print("\nCurrent word: " + display_word(word, guessed_letters))
        display_attempts(remaining_attempts, guessed_letters )

        guess = get_user_guess(guessed_letters)
        guessed_letters, remaining_attempts = update_game_state(word, guess, guessed_letters, remaining_attempts)


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

#rodesac word.txt files sheqmnit da sityvebs sheiyvant aucilebelia bolo sityvis shemdeg enter-s davachirot!

# example :

#1 ronaldo
#2 messi
#3 neymar
#4 mbappe
#5 kross
#6 antonhy
#7 benzema
#8 suarez
#9

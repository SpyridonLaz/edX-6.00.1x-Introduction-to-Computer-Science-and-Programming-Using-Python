def hangman(secretWord):
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {0:d} letters long".format(len(secretWord)))
    gameOver = False
    guessesLeft = 8
    lettersGuessed = []
    while not gameOver:
        print("-" * 11)
        print("You have {0:d} guesses left".format(guessesLeft))
        availableLetters = getAvailableLetters(lettersGuessed)
        print("Available Letters: {0:s}".format(availableLetters))
        guess = raw_input("Please guess a letter: ")
        guess = guess[0].lower()
        if len(guess)==1 and guess in string.ascii_lowercase:
            if guess in availableLetters:
                lettersGuessed.append(guess)
                if guess in secretWord:
                    response = "Good guess:"
                    if isWordGuessed(secretWord, lettersGuessed):
                        gameOver = True
                else:
                    guessesLeft -= 1
                    response = "Oops! That letter is not in my word:"
                    if guessesLeft == 0:
                        gameOver = True
            else:
                response = "Oops! You've already guessed that letter:"
        else:
        print("{0:s} {1:s}".format(response, getGuessedWord(secretWord, lettersGuessed)))
    print("-" * 11)
    if isWordGuessed(secretWord, lettersGuessed):
        print("Congratulations, you won!")
    else:
         print("Sorry, you ran out of guesses. The word was {0:s}.".format(secretWord))

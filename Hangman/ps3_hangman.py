
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    to check if the player has found the secretword
    '''
    ans = False
    for letter in secretWord:
        if letter not in lettersGuessed:
            ans = False
            break
        else:
            ans = True
    return ans

def getGuessedWord(secretWord, lettersGuessed):
    '''
    to show the letter that the player has found
    '''
    ans = ''
    for letter in secretWord:
        if letter not in lettersGuessed:
            ans += '_'
        else:
            ans += letter
    return ans

def getAvailableLetters(lettersGuessed):
    import string
    letters = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        if letter in letters:
            letters.remove(letter)
    return ''.join(letters)

def hangman(secretWord):
    print('Welcome to the game, Hangman!\nI am thinking of a word that is %d letters long.\n-------------'%(len(secretWord)))
    guessLeft = 8
    lettersGuessed = []
    Mistakemade = []
    Guessedword = '_' * len(secretWord)
    while isWordGuessed(secretWord,lettersGuessed) == False:
        guessLeft = 8 - len(Mistakemade)
        #test if we have run out of guess
        if guessLeft == 0:
            print('Sorry, you ran out of guesses. The word was %s'%(secretWord))
            break
        else:
            print('You have %d guesses left'%(guessLeft))
        #give the available letters
        print('Available Letters: %s'%(getAvailableLetters(lettersGuessed)))
        # test the new guess
        guess = input('Please guess a letter: ')
        if guess in lettersGuessed:
            print('Oops! You\'ve already guessed that letter: %s\n-------------'%(Guessedword))   
        else:
            lettersGuessed.append(guess)
            if guess not in secretWord and guess not in Mistakemade:
                Mistakemade.append(guess)
                print('Oops! That letter is not in my word: %s\n-------------'%(Guessedword)) 
            elif guess in secretWord:
                Guessedword = getGuessedWord(secretWord, lettersGuessed)
                print('Good guess: %s\n-------------'%(getGuessedWord(secretWord, lettersGuessed)))         
                
    if isWordGuessed(secretWord,lettersGuessed) == True:
        print('Congratulations, you won!')

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    correct= True
    for letter in secret_word:
        if letter in letters_guessed:
            #correct = False
            continue
        else:
            correct = False 
            return correct
    return True





    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    pass

def get_guessed_word(secret_word, letters_guessed):

    answer = ""

    for letter in secret_word:
        if letter in letters_guessed:
            answer += letter + ""
        else:
            answer += "_ "
    return answer        




    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    # pass


def is_guess_in_word(guess, secret_word):

    if guess in secret_word:
        return True
    else:
        return False 


    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word

    #pass




def spaceman(secret_word):

    #TODO: show the player information about the game according to the project spec
    
    letters_guessed =[]
    lives = 7
    alphabet = ["abcdefghijklmnopqrstuvwxyz"]


    print("Hi, Welcome to SPACEMAN!, Guess the word correctly")
    print(f"The secret word holds: {len(secret_word)} letters")
    print ("You have 7 lives,  GOOD LUCK!")
    print(secret_word)
    # print (input("Enterrrrr a Letter: "))
    print(get_guessed_word(secret_word,letters_guessed))
    #TODO: Ask the player to guess one letter per round and check that it is only one letter
   # while True:
    while lives > 0:
        this = False
        #while is_word_guessed(secret_word, letters_guessed) != True:
        while this == False:
            guess = input('Enter a letter: ').lower()
            if len(guess) != 1:
                print("PLease enter 1 letter ")
            elif guess.isalpha() == False:
                print("Please enter a letter ")
            else:
                this = True
                letters_guessed.append(guess)

                if is_guess_in_word(guess, secret_word)==True:
                    print("Your guess appears in the word")
                    if is_word_guessed(secret_word, letters_guessed):
                        print('YOU JUST WON THE GAME')
                else:
                    lives-=1
            
    #TODO: Check if the guessed letter is in the secret or not and give the player feedback
    #TODO: show the guessed word so far
        print(letters_guessed)
        print(get_guessed_word(secret_word,letters_guessed))

    #TODO: check if the game has been won or lost
        incorrect = set(letters_guessed).difference(secret_word) 
    


        if is_word_guessed(secret_word, letters_guessed):
            print('YOU JUST WON THE GAME')
            return True 
        #elif len(incorrect) > 6:
        elif lives == 0:
            print('YOU JUST LOST THE GAME \nThe word was: ' + secret_word)
            return False
        else:
            print('Incorrect Guesses: ' + str(len(incorrect)))


#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
























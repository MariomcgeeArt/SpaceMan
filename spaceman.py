import random
# my space man 


# create data structure to hold possible list of words 

def load_word():
#    f = open('words.txt', 'r')
#    words_list = f.readlines()
#    f.close()

#    words_list = words_list[0].split(' ')
   secret_word = random.choice(['cat','dogy','horse'])
   return secret_word
    
def check_userinput(user_input):
    '''checks length of user input'''
    if len(Letter) > 1 or userinput.isalpha() not True:
        return False



def show_blanks(random_word):
    '''shows blanks to user'''
    blanks = len(random_word) * '_ '
    return blanks
 


def space_man():
    lives = 6
    print("Hello, Welcome to SpaceMan\nYou have {} lives".format(lives))
    word = load_word()
    blanks = show_blanks(word)
    print(blanks)
    check_userinput()

    while lives not 0:

        



    return blanks



space_man()
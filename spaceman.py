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

def fill_inblanks(secret_word, blanks,Letter):

        for i in range(len(secret_word)):
                if secret_word[i] == Letter:
                        blanks[i] = secret_word[i]
        
        return blanks

                

        

       
  







def guessed_correct(Letter, secret_word):
        return True if Letter in secret_word else False

        
                
        

        
        







def user_input():
    '''checks length of user input'''
    Letter = input("Enter a Letter ")
    if len(Letter) > 1 or Letter.isalpha() is False:
        print('Please Enter a letter ')
        user_input()
    else:
      return Letter 



def show_blanks(random_word):
    '''shows blanks to user'''
    blanks = len(random_word) * '_ '
    return blanks
 


def space_man():
    lives = 6
    print("Hello, Welcome to SpaceMan\nYou have {} lives".format(lives))
    word = load_word()
    blanks = show_blanks(word)
    print (blanks)
    Letter = user_input()






    while lives is not 0:
            if guessed_correct(Letter, word): 
                    fill_inblanks(word,blanks,Letter)



    return blanks



space_man()

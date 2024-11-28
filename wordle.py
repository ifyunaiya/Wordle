import random
     
random_word = random.choice(open("wordle_words.txt").readlines()).strip()
answer = list(random_word)
result = []

def rightplace(guess):
    """
    :param guess:
    :return: which characters in your guessed word
     are at the right place and what character it is
    """
    rightplace = 0
    see_char = ''
    character_to_string = ''
    correct_characters = []#used in main.py so program can see what character in guess is correct
    for i in range(len(answer)):
        if answer[i] == guess[i]:
            rightplace = rightplace+1
            see_char = guess[i]
            correct_characters.append(see_char)

    return rightplace, correct_characters


def wrongplace(guess):
    """
        :param guess:
        :return: which characters in your guessed word
         are at the wrong place and what character it is
        """
    notrightplace = 0
    see_char = ''
    incorrect_characters = []
    character_to_string = ''
    for i in range(len(answer)):
        if answer[i] != guess[i]:
            for j in range(len(guess)):
                if answer[i] == guess[j] and guess[j] != answer[j]:
                    #print(answer[i])
                    notrightplace += 1
                    see_char = guess[j]#used in main.py so program can see what character in guess is incorrect
                    incorrect_characters.append(see_char)

                    break
            
    return notrightplace, incorrect_characters
    
def main():
  guess_num = 0
  
  for guess_num in range(1,10):
   guess = input("Guess a five letter word ").upper()
   
   if len(guess)!= 5:
      print("try again")
      
      
   elif len(guess)== 5:
    guess = list(guess)
    right_place, corr_char_r = rightplace(guess)
    wrong_place, corr_char_w = wrongplace(guess)
    result = [right_place,wrong_place]
    
    if (result[0],result[1]) != [5,0]:
     print("Guess number:",guess_num+1,"")
     print(result)
     guess_num += 1
    
    else:
     print('You got it right, Well done!')
     break
       
    if guess_num == 10:
     print(f"Maximum attempts reached, the correct answer was: {random_word}")
     
if __name__ == '__main__':
 main()






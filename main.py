import wordle as wd
from wordle import answer
import random

def guess(a_list):
    """
    guesses a random word from
    a_list which could be the contents of the file or the contents of the filtered list
    :param a_list:
    :return: guessed word as a list
    """

    guess_list = []
    random_word = random.choice(a_list)

    for i in range(0, len(random_word)):
        guess_list.append(random_word[i])
    return guess_list

def filter_list(a_list,guess_word, corr_char_r, corr_char_w):
    """
    :param a_list: the list to filter out words from
    :param guess_word: not being used but it is the word that was last guessed
    :param corr_char_r: It is characters in the word that are in the correct place
    :param corr_char_w: It is characters in the word that are in the wrong place
    :return: a list containing words that have the answer to be selected from
    """

    new_list = []

    filtered_list = [] #This stores all the words in the list of words that contain characters that are correct
                        # and in the right place or that are correct and in the wrong place

    valid_words = corr_char_r + corr_char_w

    for item,row in enumerate(a_list):
        for index2,character in enumerate(valid_words):
            if character in row and row not in filtered_list:
                filtered_list.append(row)


    #from the filtered list, i further check which words in the filtered list are at the same index position
    # as the words in the guessword
    for row in filtered_list:
        for index2, char2 in enumerate(guess_word):
            if char2 in row and row[index2] == char2:
                #print(f'{char2} at{i}')
                new_list.append(row)
            # elif char2 not in row:
            #     new_list.pop(row)

        for index2, char2 in enumerate(guess_word):
            if char2 in row and row[index2] != char2 and row not in new_list:
                # print(f'{char2} at{index2}')
                new_list.append(row)


    print('The new list gotten from filtering contains:',new_list)

    return new_list


def main():
    content_list = []

    with open('wordle_words.txt', 'r') as file:
        line_list = file.readlines()
        for line in line_list:
            contents = line.strip('\n')
            content_list.append(contents)

    print('I am ready to guess your word')

    guess_word = guess(content_list)
    guess_word_to_str = ''.join(map(str, guess_word))
    print('My guess is', guess_word_to_str)


    right_place, corr_char_r = wd.rightplace(guess_word)
    wrong_place, corr_char_w = wd.wrongplace(guess_word)

    result = [right_place, wrong_place]
    guess_no = 0
    print(result)

    while result != [5,0] and guess_no < 10 :
        filtered_list = filter_list(content_list, guess_word, corr_char_r, corr_char_w)

        guess_word = guess(filtered_list)
        guess_word_to_str = ''.join(map(str, guess_word))

        print('the answer is ', answer)
        print('My guess is', guess_word_to_str)
        print(result)
        print('-------------------')

        right_place, corr_char_r = wd.rightplace(guess_word)
        wrong_place, corr_char_w = wd.wrongplace(guess_word)

        result = [right_place, wrong_place]

    guess_no +=1

main()

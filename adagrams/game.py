import random
import copy

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

SCORE_CHART = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
}

def draw_letters():

    drawn_letters = []
    letter_pool_copy = copy.deepcopy(LETTER_POOL)
    counter = 0
    
    while counter < 10: 
        letter, count = random.choice(list(letter_pool_copy.items()))
        print(letter, count)
        if count == 0:
            continue
        else:
            #decrement count by indexing the dictionary
            letter_pool_copy[letter] -= 1
            #add to drawn letters by calling it
            drawn_letters.append(str(letter))
            counter += 1
    
    return drawn_letters

def uses_available_letters(word, letter_bank):
    letter_bank_copy = copy.deepcopy(letter_bank)
    for letter in word.upper(): 
        if letter not in letter_bank_copy:
            return False
        else:
            letter_bank_copy.remove(letter)
    return True


def score_word(word):
    total_score = 0
    for letter in word.upper():
        # get the points ie value from SCORE_CHART dictionary
        total_score += SCORE_CHART.get(letter) 
    if len(word) > 6 and len(word) <= 10:
        total_score += 8
    return total_score


def get_highest_word_score(word_list):
    
    max_score = 0
    max_word = ""

    #call function to get score
    for word in word_list:
        current_score = score_word(word)
        if current_score < max_score:
            continue
        elif current_score > max_score:
            max_score = current_score
            max_word = word
        else:
            #TIE CONDITIONS - len is the same 
            if len(word) == len(max_word):
                continue
            elif len(word) == 10:
                max_word = word
                max_score = current_score    
            elif len(word) < len(max_word) and len(max_word) != 10:
                max_word = word
                max_score = current_score 
            else:
                continue
            
    return [max_word, max_score]

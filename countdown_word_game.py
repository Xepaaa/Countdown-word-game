import time
import random

vowels = ["A","E","I","O","U"]
consonants = ["B", "C", "D", "F", "G", "J", "K", "L", "M", "N", "P", "Q", "S", "T", "V", "X", "Z"]

chosen_letters = []

attempt = 18

print("Welcome to my version of the Countdown Word Game!")
print("\nChoose a series of vowel and consonant options to build a list to make words from.")
print("As an additional challenge, you cannot use the same letter twice nor submit a word shorter than 3 letters.")
print("\nHave fun!")

while True:
    ready_to_play = input("\nAre you ready to play? (Y/N): ")
    
    while len(chosen_letters) != 18 and ready_to_play[0].lower() == "y":

        print(f"\n{attempt} attempts left")
        chosen_letter = input("\nPlease choose a vowel or a consonant (V/C): ")

        if chosen_letter[0].lower() == "v":
            attempt = attempt - 1
            chosen_letters.append(random.choice(vowels))

        elif chosen_letter[0].lower() == "c":
            attempt = attempt - 1
            chosen_letters.append(random.choice(consonants))
        else:
            print("\nThat's an incorrect input, please enter V or C")

        print("\nYou currently have the following letters in the bank:")
        print(chosen_letters)
    
    if ready_to_play[0].lower() == "n":
        print("\nOkiie, signing out :)")
        break
        
    elif len(chosen_letters) == 18:
        
        print("\nRighty then, now try to form at least 5 words with the letters you have accumulated >")
        count = 5
        playing = True
        words_list = []
        
        while playing and len(words_list) < 5:
            
            print("\nWords remaining: {}".format(count))
            
            word_attempt = input("\nEnter a word: ").upper()
            
            word_attempt = list(word_attempt)
            
            similar = set(chosen_letters).intersection(word_attempt)
            
            if len(word_attempt) == len(similar) and len(word_attempt) >= 3:
                count -= 1
                words_list.append(word_attempt)
                print("\nAccepted")
            else:
                time.sleep(1)
                print("\nCan't make that word given the vast selection of letters...")
                
        if len(words_list) == 5:
            time.sleep(2)
            print("\nWell done, that concludes it, you successfully came up with the following five words: ")
            print(words_list)
            print("\nThanks for playing <3")
            break

"""
import itertools
words_list = [['M', 'A', 'T', 'E'], ['M', 'A', 'T', 'E'], ['M', 'A', 'T', 'E'], ['M', 'A', 'T', 'E'], ['M', 'A', 'T', 'E']]
s = list(itertools.chain(*words_list))

def convert(s):
    
    new = ""
    
    for x in s:
        new += x
    return new

print(convert(s))
"""
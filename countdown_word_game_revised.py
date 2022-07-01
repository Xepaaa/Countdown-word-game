import time
import random
from english_words import english_words_lower_alpha_set


def validate(word, chosen_letters):
    
    return all(letter in chosen_letters for letter in word)


def shuffle_or_play(letters,letters1):
    
    
    while True:
        
        choice = input("\nWould you like to shuffle the list of letters or enter a word? (S/W) ").lower()
        
        if choice == "s":
            print("\nShuffling...")
            time.sleep(2.3)
            random.shuffle(letters)
            return letters
    
        elif choice == "w":
            return letters1
        else:
            print("\nPlease enter either S or W...")
            continue


def ready_up():
    
    while True:
        
        play = input("\nAre you ready to play? (Y/N) ")
        
        if play.lower() == "y" or play.lower() == "yes" or play.lower() == "Yes" or play.lower() == "Y":
            return True
        elif play.lower() == "n" or play.lower() == "no" or play.lower() == "No" or play.lower() == "N":
            return False
        else:
            print("\nSorry, please enter Y or N...")
            continue


complimentos = ["Well done","That's correct","Input accepted","That counts","Excellent"]
downies = ["Not a word pal","Nopes","Input rejected","That does not count","Try again"]


vowels = ["A","E","I","O","U"]
consonants = ["B", "C", "D", "F", "G", "J", "K", "L", "M", "N", "P", "Q", "S", "T", "V", "X", "Z"]

chosen_letters = []

attempt = 18

print("Welcome to my version of the Countdown Word Game!")
print("Choose a series of vowel's and consonant's to build a list of letters to make words from and attempt to come up with 5 words!")
print("\nHave fun!")

ready_to_play = ready_up() 

while len(chosen_letters) != 18 and ready_to_play:

    print(f"\n{attempt} selections left")
        
    chosen_letter = input("\nPlease choose a vowel or a consonant (V/C): ")

    if chosen_letter.lower() == "v":
        attempt -= 1
        chosen_letters.append(random.choice(vowels))
        print("\nYou currently have the following letters in the bank:")
        print(chosen_letters)

    elif chosen_letter.lower() == "c":
        attempt -= 1
        chosen_letters.append(random.choice(consonants))
        print("\nYou currently have the following letters in the bank:")
        print(chosen_letters)
    
    else:
        print("\nThat's an incorrect input, please enter V or C")
        

    while len(chosen_letters) == 18:
   
        print("\nRighty then, now try to form 5 words with the letters you have accumulated!")

        count = 5
        words_list = []
        lowered_letters = map(str.lower,chosen_letters)
        lowered_letters_list = list(lowered_letters)

        while len(words_list) != 5:
            
            shuffled_or_not_chosen_letters = shuffle_or_play(chosen_letters,chosen_letters)

            print("\n",shuffled_or_not_chosen_letters)
            print("\nWords to fulfill: {}".format(count))
            word_attempt = input("\nEnter a word: ").lower()

            if word_attempt in english_words_lower_alpha_set and validate(word_attempt, lowered_letters_list) and word_attempt not in words_list and len(word_attempt) > 2:
                print("\n",random.choice(complimentos))
                count -= 1
                words_list.append(word_attempt)
            elif word_attempt in words_list:
                print("\nYou have already entered that word :O")
            elif word_attempt not in english_words_lower_alpha_set:
                print("\n",random.choice(downies))
            elif len(word_attempt) < 3:
                print("\nThat's too short :/")
            else:
                print("\nYou cant form that word with your selection of letters...")


        print("\nThat concludes the word game!, you successfully came up with the following five words... ")
        time.sleep(3)
        wordies = (', '.join(words_list))
        print("Words found: ",wordies)
        break
    
    
print("\nThanks for playing <3")


# :)
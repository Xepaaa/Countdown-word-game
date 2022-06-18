# Countdown-word-game

My (bad) version of the Countdown word game :)

so the idea was to recreate the countdown word game as it appears on the TV show.
I thought of this idea this morning thinking it would only take a few hours but ended up being more difficult than i expected.
Nevertheless, i continued with the project and now have a functioning game, also having learnt quite alot in the process :)

A few things that definitely need improving in this game are listed as following:

1 - There needs to be a more sophisticated word checker, one that allows mutiple letters from the list to be used to make the word,
i tried a few different methods to check for a match but using a set().intersection() method was the one i went with.

2 - The words submitted need to be checked against eachother in order to determine if they are being repeated, this is a huge flaw of the game.

3 - The way the submitted words are presented at the end is as a list within a list, in which the letters of the words are separate still. This can just pass
but is not visually appealing. I tried to correct it by flattening using the following block of code but didn't know how to ensure the original words stay separate:

        import itertools
        words_list = [['M', 'A', 'T', 'E'], ['M', 'A', 'T', 'E'], ['M', 'A', 'T', 'E'], ['M', 'A', 'T', 'E'], ['M', 'A', 'T', 'E']]
        s = list(itertools.chain(*words_list))

        def convert(s):

            new = ""

            for x in s:
                new += x
            return new

print(convert(s))

4 - Lastly, players can enter any combination of letters that appear in their chosen_list and their isnt a check in place to ensure that their submission is actually a word.
Obviously its impossible to hold a dictionary of words in place to compare the word against but if it were possible to match the submission against words on the web there
is a possibility for a check. Potentially learning about webscraping will allow me the necessary skills to refine this code.

All in all, this was a fun little project from which i learned alot :D

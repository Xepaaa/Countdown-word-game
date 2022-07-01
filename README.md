# Countdown-word-game

My (bad) version of the Countdown word game :)

----- EDIT BELOW -----

so the idea was to recreate the countdown word game as it appears on the TV show.
I thought of this idea this morning thinking it would only take a few hours but ended up being more difficult than i expected.
Nevertheless, i continued with the project and now have a functioning game, also having learnt quite a lot in the process :)

A few things that definitely need improving in this game are listed as following:

1 - There needs to be a more sophisticated word checker, one that allows multiple letters from the list to be used to make the word,
i tried a few different methods to check for a match but using a set().intersection() method was the one i went with.

2 - The words submitted need to be checked against each other in order to determine if they are being repeated, this is a huge flaw of the game.

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

4 - Lastly, players can enter any combination of letters that appear in their chosen_list and there isnt a check in place to ensure that their submission is actually a word.
Obviously its impossible to hold a dictionary of words in place to compare the word against but if it were possible to match the submission against words on the web there
is a possibility for a check. Potentially learning about webscraping will allow me the necessary skills to refine this code.

All in all, this was a fun little project from which i learned a lot :D




<<<<< EDIT >>>>>

This game has been improved massively, hence this edit to explain what was changed and how i went about it!

Below is a list of all the improvements that have been made to the game:

- User submitted word validation;
So, the main reason i revisited this project was after coming across a package known as english-words. This package "Contains sets of English words from svnweb.freebsd.org/csrg/share/dict/. This is up to date with revision 61569 of their words list", given the fact that this is a word game in which players have to form words... this proved to be vital for realistic gameplay. I made it a conditional requirement for the word input to be within a set of aforementioned package - this is by far the best improvement for the game.

- Proper letters to list checks;
Another major issue in the game was that the user could not enter the same letter twice, this was because due to the use of the set().intersection() method. I accommodated for this flaw by challenging the user to not use the same letter twice, however, this was not how the game was intended to be played. I now have a solid validation function in place that checks the word entered against the letter in the list.

- Word vs word check;
Although this is a minor improvement, its essential for flawless gameplay. Words entered are checked against the words already accumulated to ensure a unique word is entered each time.

- Final words presentation list;
The way in which all the words input by the user are presented at the end of the game was not appealing at all (list, within a list), i have changed it so that the words appear as strings in a neat format using the .join() method.

- To shuffle or play?;
A function which asks the player whether they would like to enter a word, or first shuffle the list has been implemented. This function was challenging to get right at first as i kept receiving "None" as its return value. I fixed this error by passing two arguments of the same list of letters into the shuffle or play function, this allowed me to return two different values to be used in the main code. The shuffled list is retained until shuffled again.

- Ready up & list of cheers and jeers (not harsh);
With respect to a couple of minor improvements, i added a function to initially ask the player if they are ready. Moreover, upon getting a word correct or incorrect there is a message picked from a list consisting of positive and negative feedback, respectively.


I'm really pleased with these improvements and was glad i found a useful package to make the game realistic :)

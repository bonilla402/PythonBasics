def print_upper_words(words):
    """For a list of words, print out each word on a separate line, 
       but in all uppercase. How can you change a word to uppercase? 
       Ask Python for help on what you can do with strings!
    """


    for word in words:
        print(word.upper())


def print_upper_words2(words):
    """For a list of words, print out each word on a separate line, 
       but in all uppercase. Only if it starts with e
    """

    for word in words:
        upperWord =  word.upper()
        if upperWord.startswith("E"):
            print(upperWord)

def print_upper_words3(words, starters):
    """For a list of words, print out each word on a separate line, 
       but in all uppercase. Only if it starts with one of the passed letters on starters
    """

    for word in words:
        upperWord =  word.upper()
        for startLetter in starters:
            if upperWord.startswith(startLetter.upper()):
                print(upperWord)
                break

print_upper_words(["uno","dos","Tres"])  
print_upper_words2(["Easter","uno","Elantris", "dos","Tres"])     
print_upper_words3(["Easter","uno","Elantris", "dos","Tres"], ["e","t"])     
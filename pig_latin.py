#!/usr/bin/env python3

#COP2002.0M1 Programming Logic
#Module 10 Project 10-1 Pig Latin Translator Program
#Submitted by Richard Ruth

# Program obtains statement from user and translates to pig latin using following rules:
# 1) Statement is translated to lowercase
# 2) Punctuation is stripped
# 3) Per rubrics, it is assumed words separated by single space
# 4) If word starts with vowel, 'way' is added to end of word
# 5) If word starts with consonant, all consanants that appear before first vowel are moved to end of word, and then 'ay' added
# 6) If words starts with a 'y', the 'y' is treated as a consonant. If 'y' appears anywhere else in word, it is treated as a vowel

def main():

    # Main module calls functions for obtaining user input, translation of the input, and displays output

    print("\nPig Latin Translator\n")
    choice = "y"
    while choice.lower() == "y":
        statement = get_text()
        print("English:    ", statement)
        statementFinal = translation(statement)
        print("Pig Latin:  ", statementFinal)
        print()
        choice = input("Continue? (y/n): ")
    print()
        
# Function get_text obtains user input, strips any leading or trailing whitespace, calls function to strip punctuation
#  calls function to convert to lower case, and then returns statement for "English" output line

def get_text():
    statement = input("\nEnter text:  ")
    statement = statement.strip()
    statement = strip_punctuation(statement)
    statement = statement.lower()
    return statement

# Function strip_punctuation strips user inputted statement of any normal grammar punctuation

def strip_punctuation(statement):
    punctuationList = '''!;:'",.?~'''
    statementStripped = ""
    for char in statement:
        if char not in punctuationList:
            statementStripped = statementStripped + char
    return statementStripped

# Function translation converts formatted statement into pig latin per rules in comments above

def translation(statement):
    vowelListStart = ['a', 'e', 'i', 'o', 'u']
    vowelListY = ['a', 'e', 'i', 'o', 'u', 'y']
    statement = statement.split()
    for words in range(len(statement)):
        letters = statement[words]
        if letters[0] in vowelListStart:
            statement[words] = letters + 'way'
        else:
            for i in range (len(letters)):
                if letters[i] not in vowelListY:
                    i += 1
                else:
                    statement[words] = letters[i:] + letters[:i] + 'ay'
                    break
    return ' '.join(statement)           
            
# If this module is the main module, call the main() function

if __name__ == "__main__":
     main()
     

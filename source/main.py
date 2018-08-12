"""Entry point of application"""

from thesaurus import Word
import random

print("Welcome to py-synonyms! Please ensure you have an Internet connection.")
print("Enter '0' to exit. \n")

def handle_input():
    print("Please enter a word or sentence.")

    console = input()

    if console == '0':
        pass
    else:
        print("\nContacting thesaurus.com...")
        # Parse sentence into separte words
        words = console.split(' ')
        # Search for synonyms in thesaurus.com
        syns = []
        print("")
        for item in words:
            # Choose a random synonym for each word
            synonyms = Word(item).synonyms()
            if len(synonyms) > 0:
                to_add = random.choice(synonyms)
            else:
                to_add = item
            print(item + " -> " + to_add)
            syns.append(to_add)

        # Create a string from the synonyms
        sentence = ' '.join(syns)
        print("Similar sentence: " + sentence + "\n")
        handle_input()

# Start the program
handle_input()

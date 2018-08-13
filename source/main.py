"""Entry point of application"""

from thesaurus import Word
import random
import math

relevancy = 0
relevancy_dict = {0: "Extremely relevant (default)",
                  1: "Relevant",
                  2: "Less relevant",
                  3: "Random"}

print("Welcome to py-synonyms! Please ensure you have an Internet connection.")
print("Type '-h' for help.")
print("Enter '0' to exit. \n")

def show_help():
    print("List of commands:\n")
    # Print information about '-r' command
    print("'-r [integer]': Set the relevancy of chosen synonyms")
    for key in relevancy_dict:
        print(str(key) + " - " + relevancy_dict[key])
    # Print help menu information
    print("\n'-h': Show help menu")
    # Print info about quitting script
    print("\nEnter '0' to exit\n")

def choose_syn(item):
    # Choose a random synonym for each word
    synonyms = Word(item).synonyms()
    to_return = ""
    if len(synonyms) > 0:
        if relevancy == 0:
            # Choose first synonym
            to_return = synonyms[0]
        elif relevancy == 1:
            # Choose the top 20% relevant synonyms
            top_20 = math.ceil(len(synonyms) * .2)
            new_list = synonyms[0:top_20]
            to_return = random.choice(new_list)
        elif relevancy == 2:
            # Choose the top 40% relevant synonyms
            top_40 = math.ceil(len(synonyms) * .4)
            new_list = synonyms[0:top_40]
            to_return = random.choice(new_list)
        elif relevancy == 3:
            # Choose a random synonym
            to_return = random.choice(synonyms)
    else:
        to_return = item
    print(item + " -> " + to_return)
    return to_return

def handle_input():
    print("Please enter a sentence or command.")

    console = input()

    if console == '0':
        # Quit the script
        pass
    elif console[0] == '-':
        # A command has been issued
        if console == '-h':
            # Show the help menu
            show_help()
            handle_input()
        elif console[0:2] == '-r':
            # Set the relevancy of synonyms
            if len(console) == 4:
                if int(console[3]) >= 0 and int(console[3]) < len(relevancy_dict):
                    global relevancy
                    relevancy = int(console[3])
                    print("Synonym relevancy changed: %d: %s" % (relevancy, relevancy_dict[relevancy]))
                    print("")
                else:
                    print("Invalid range.\n")
            else:
                print("Invalid syntax.\n")
            handle_input()
        else:
            print("Invalid command.\n")
            handle_input()
    else:
        # Process a sentence
        print("\nSynonym relevancy set to %d: %s" % (relevancy, relevancy_dict[relevancy]))
        print("Contacting thesaurus.com...\n")
        # Parse sentence into separte words
        words = console.split(' ')
        # Search for synonyms in thesaurus.com
        syns = []
        for item in words:
            syns.append(choose_syn(item))

        # Create a string from the synonyms
        sentence = ' '.join(syns)
        print("Similar sentence: " + sentence + "\n")
        handle_input()

# Start the program
handle_input()

# py-synonyms
A simple script that scrapes [thesaurus.com](https://www.thesaurus.com/) for the synonyms in a sentence, and creates a similar string from it. There are different degrees of synonym relevancy that the script can work with, ranging from **extremely relevant** (first synonym) to **random** (any synonym). The degree can be set for each session with a command. Due to the amount of synonyms stored on the for each word, using any degree lower than the first will quickly lead to sentences that make very little sense. An Internet connection is required. 

Note that any words with special characters (won't, hasn't, etc.) are not stored in the thesaurus. To input these words, omit any markings.

## Getting started
To get started, use 'pip install -r requirements.txt' to install any dependencies. Then, simply run 'python3 main.py' in a terminal. 

## Libraries
[Thesaurus API](https://github.com/Manwholikespie/thesaurus)

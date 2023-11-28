# define a function that can read a txt file
# into a list (of strings)

def read_file(filename : str) -> list :
    with open(filename, "r") as filelines:
        lines = filelines.read().splitlines()
    return lines

# make sure to use the current working directory of our main script
import os
# Get the current script directory
directory = os.path.dirname(os.path.realpath(__file__))

nouns_file = os.path.join(directory, 'nouns.txt')
adjectives_file = os.path.join(directory, 'adjectives.txt')

nouns = read_file(nouns_file)
adjectives = read_file(adjectives_file)
#print(nouns)
#print(adjectives)
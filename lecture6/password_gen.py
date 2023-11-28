import file_reader
import os
import random
import string

# Get the current script directory
directory = os.path.dirname(os.path.realpath(__file__))
nouns_file = os.path.join(directory, 'nouns.txt')
adjectives_file = os.path.join(directory, 'adjectives.txt')

# while the user asks for more passwords ...
# create a new password and print it
nouns = file_reader.read_file(nouns_file)
adjectives = file_reader.read_file(adjectives_file)

def generate_password(nouns, adjectives):
    # Draw an adjective
    adj = random.choice(adjectives)

    # Draw a noun
    noun = random.choice(nouns)

    # Draw a random number between 0 and 100
    rand_number = random.randint(0, 100)

    # Draw a special character
    special_chars = string.punctuation
    char = random.choice(special_chars)

    # combine and return
    return adj + noun + str(rand_number) + char

stop = False
while not stop: 
    password = generate_password(nouns, adjectives)
    print("Your password is:", password)
    stop = input("Stop? (y|n)") == "y"
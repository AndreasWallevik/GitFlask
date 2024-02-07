import random
def get_shuffled_word():
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()
    if words:
        return random.choice(words)
    return "No words were found"

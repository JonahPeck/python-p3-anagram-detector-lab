# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word_letters = sorted(letter for letter in word)

    def match(self, word_list):
        match_world_list = []

        for word in word_list:
            if sorted([letter for letter in word]) == self.word_letters:
                match_world_list.append(word)

        return match_world_list

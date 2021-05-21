import random

class Hangman:
    possible_words = ['becode', 'learning', 'mathematics', 'sessions']
    word_to_find = ""
    hidden_word = []
    lives = 5
    letter = ''
    number_of_words = 0
    correctly_guessed_letters = []
    wrongly_guessed_letters = []
    turn_count = 0
    error_count = 0

    def init_my_function(cls):
        cls.number_of_words = len(cls.possible_words) - 1
        cls.word_to_find = cls.possible_words[random.randint(0, cls.number_of_words)]
        cls.hidden_word = '_' * len(cls.word_to_find)
        print(" ".join(list(map(str,cls.hidden_word))))
        print('')

    def start_game(cls):
        cls.init_my_function()
        cls.play()

    def print_my_round(cls):
        print(" ".join(list(map(str,cls.hidden_word))))
        print('\n')
        print(f"Wrongly guessed letter --> {cls.wrongly_guessed_letters}.")
        print(f"Correctly guessed letter --> {cls.correctly_guessed_letters}.")
        print(f"Number of lives remaining --> {cls.lives}.")
        print(f"Error Count --> {cls.error_count}.")
        print(f"Turn Count --> {cls.turn_count}.")

    def game_over():
        print("GAME OVER ...")

    def well_played(cls):
        print(f"You found the word: {cls.word_to_find} in {cls.turn_count} turn with {cls.error_count} errors!")

    def check_letter(cls):
        if len(cls.letter) != 1:
            print("Please, insert only one character")
            return 1
#    def check_end_of_game(cls):
#        if c

    def play(cls):
        while (cls.lives) != 0:
            cls.letter = input("Please enter a letter: ")
            cls.print_my_round()

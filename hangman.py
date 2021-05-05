import random as random
import file_reader as file_reader

IS_RUNNING = True
TRIES = 6
FILE_WITH_WORDS = "countries-and-capitals.txt"

list_of_words = file_reader.read_file_to_list(FILE_WITH_WORDS)


def preparing_word_to_answer():
    underscores = []
    chosen_word = list_of_words[random.randint(0, len(list_of_words) - 1)]

    for i in range(len(chosen_word)):
        underscores.append("_")

    return chosen_word, underscores


def check_if_letter_exist(user_input, chosen_word, underscores):
    global TRIES
    chosen_word = list(chosen_word)
    if user_input in chosen_word:
        index_of_char = []

        for i in range(len(chosen_word)):
            if chosen_word[i] == user_input:
                index_of_char.append(i)

        for item in index_of_char:
            underscores[item] = chosen_word[item]
    else:
        TRIES -= 1


def check_game_status(chosen_word, underscores):
    if TRIES >= 1:
        if list(chosen_word) == underscores:
            print("\n")
            print("Correct word was: " + chosen_word)
            print("You win!")
            return False
        else:
            return True
    else:
        print("\n")
        print("Correct word was: " + chosen_word)
        print("You loose")
        return False


def main_game(is_running):
    chosen_word, underscores = preparing_word_to_answer()

    print("Welcome to simply Hangman!")
    print("Category of words are capitals of countries")

    while is_running:
        print(f"""
        
Tries left: {str(TRIES)}
        
        """)

        underscores_to_print = " ".join([str(elem) for elem in underscores])
        print(underscores_to_print)
        print("\n")
        user_input = input('Please give me your guess: ')
        check_if_letter_exist(user_input, chosen_word, underscores)
        is_running = check_game_status(chosen_word, underscores)


main_game(IS_RUNNING)

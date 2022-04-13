#############################
# HangMan by PanzerKrzysiek #
#############################

"""   The main file of the HangMan game.   """

# Built-in Python libraries
from random import choice
from os import system
from time import sleep as delay
# Program modules
from modules.letters import *
from modules.list import *
from modules.resources import *

# Program variables
word = ""
word_list = []
lenght = len(word)
guess = ""
money = 200
used_letters = []

# Functions
def batch(batch_command):
    system(batch_command)

def cls():
    batch("cls")

def pause():
    print("Naciśnij dowolny przycisk, aby kontynuować.")
    batch("pause>nul")
    print("")

# Command prompt preparation
batch("title HangMan by PanzerKrzysiek")
batch("color 0E")

cls()

# Greeting message
print("Witaj w grze HangMan!")
delay(2.5)
print("")

def generate_word():
    global word, word_list, lenght
    word = choice(list_of_words)
    word_list = ["_" for lenght in word]
    lenght = len(word)

generate_word()

# Main loop
while True:
    cls()
    if "".join(word_list) == word.upper() \
    and "_" not in "".join(word_list):
        print("GRATULACJE, wygrałeś/aś!")
        print(f"Hasłem było słowo {word.upper()}.")
        print(f"Końcowy budżet: {money} zł.")
        print("")
        print(game_ended_message)
        try:
            game_ended_user_choice = int(input("> "))
        except:
            print("BŁĄD! Nieprawidłowa informacja wejścia.")
            pause()
            continue
        if game_ended_user_choice == 1:
            cls()
            print("Generowanie nowej gry...")
            delay(2.5)
            generate_word()
            money = 200
            used_letters = []
        elif game_ended_user_choice == 2:
            quit()
    if money <= 0:
        print("PRZEGRAŁEŚ/AŚ!")
        print(f'Hasłem było słowo "{word.upper()}".')
        print(f"Końcowy budżet: {money} zł.")
        print("")
        print(game_ended_message)
        try:
            game_ended_user_choice = int(input("> "))
        except:
            print("BŁĄD! Nieprawidłowa informacja wejścia.")
            pause()
            continue
        if game_ended_user_choice == 1:
            cls()
            print("Generowanie nowej gry...")
            delay(2.5)
            generate_word()
            money = 200
            used_letters = []
        elif game_ended_user_choice == 2:
            quit()
    else:
        pass
    cls()
    print(" ".join(word_list))
    print(f"Budżet: {money} zł.")
    print("")
    print(loop_choice_message)
    user_choice = ""
    try:
        user_choice = int(input("> "))
    except:
        pass
    if user_choice == 1:
        print("")
        print("Wprowadź dowolną spółgłoskę polskiego alfabetu.")
        guess = input("> ")
        word_control = \
            [a for a, b in enumerate(word.upper()) if b == guess.upper()]
        if len(guess) == 1:
            if guess.upper() in consonants and guess.upper() not in vowels:
                if guess.upper() in word.upper():
                    if guess.upper() not in used_letters:
                        for i in word_control:
                            word_list[i] = guess.upper()
                        used_letters.append(guess.upper())
                        money += 100
                    else:
                        pass
                else:
                    if guess.upper() not in used_letters:
                        used_letters.append(guess.upper())
                        money -= 20
                    else:
                        money -= 20
            else:
                print("BŁĄD! Podaj dowolną spółgłoskę polskiego alfabetu.")
                pause()
        elif len(guess) == 0:
            pass
        else:
            print("BŁĄD! Podaj tylko jedną spółgłoskę polskiego alfabetu.")
            pause()
    elif user_choice == 2:
        cls()
        print(f"Twój budżet: {money} zł.")
        print(vowel_buying_message)
        user_vowel_buy_choice = input("> ")
        if user_vowel_buy_choice == "1" \
        or user_vowel_buy_choice == "A" \
        or user_vowel_buy_choice == "a":
            word_c_a = [a for a, b in enumerate(word.upper()) if b == "A"]
            if "A" not in used_letters:
                if money >= 150:
                    money -= 150
                    used_letters.append("A")
                    if "A" in word.upper():
                        for i in word_c_a:
                            word_list[i] = "A"
                        money += 160
                    else:
                        money -= 10
                else:
                    print("BŁĄD! Masz za mało pieniędzy.")
                    pause()
            else:
                print("BŁĄD! Wybrana litera została wcześniej użyta.")
                pause()
        elif user_vowel_buy_choice == "2" \
        or user_vowel_buy_choice == "Ą" \
        or user_vowel_buy_choice == "ą":
            word_c_ą = [a for a, b in enumerate(word.upper()) if b == "Ą"]
            if "Ą" not in used_letters:
                if money >= 50:
                    money -= 50
                    used_letters.append("Ą")
                    if "Ą" in word.upper():
                        for i in word_c_ą:
                            word_list[i] = "Ą"
                        money += 60
                    else:
                        money -= 10
                else:
                    print("BŁĄD! Masz za mało pieniędzy.")
                    pause()
            else:
                print("BŁĄD! Wybrana litera została wcześniej użyta.")
                pause()
        elif user_vowel_buy_choice == "3" \
        or user_vowel_buy_choice == "E" \
        or user_vowel_buy_choice == "e":
            word_c_e = [a for a, b in enumerate(word.upper()) if b == "E"]
            if "E" not in used_letters:
                if money >= 120:
                    money -= 120
                    used_letters.append("E")
                    if "E" in word.upper():
                        for i in word_c_e:
                            word_list[i] = "E"
                        money += 130
                    else:
                        money -= 10
                else:
                    print("BŁĄD! Masz za mało pieniędzy.")
                    pause()
            else:
                print("BŁĄD! Wybrana litera została wcześniej użyta.")
                pause()
        elif user_vowel_buy_choice == "4" \
        or user_vowel_buy_choice == "Ę" \
        or user_vowel_buy_choice == "ę":
            word_c_ę = [a for a, b in enumerate(word.upper()) if b == "Ę"]
            if "Ę" not in used_letters:
                if money >= 50:
                    money -= 50
                    used_letters.append("Ę")
                    if "Ę" in word.upper():
                        for i in word_c_ę:
                            word_list[i] = "Ę"
                        money += 60
                    else:
                        money -= 10
                else:
                    print("BŁĄD! Masz za mało pieniędzy.")
                    pause()
            else:
                print("BŁĄD! Wybrana litera została wcześniej użyta.")
                pause()
        elif user_vowel_buy_choice == "5" \
        or user_vowel_buy_choice == "I" \
        or user_vowel_buy_choice == "i":
            word_c_i = [a for a, b in enumerate(word.upper()) if b == "I"]
            if "I" not in used_letters:
                if money >= 100:
                    money -= 100
                    used_letters.append("I")
                    if "I" in word.upper():
                        for i in word_c_i:
                            word_list[i] = "I"
                        money += 110
                    else:
                        money -= 10
                else:
                    print("BŁĄD! Masz za mało pieniędzy.")
                    pause()
            else:
                print("BŁĄD! Wybrana litera została wcześniej użyta.")
                pause()
        elif user_vowel_buy_choice == "6" \
        or user_vowel_buy_choice == "O" \
        or user_vowel_buy_choice == "o":
            word_c_o = [a for a, b in enumerate(word.upper()) if b == "O"]
            if "O" not in used_letters:
                if money >= 100:
                    money -= 100
                    used_letters.append("O")
                    if "O" in word.upper():
                        for i in word_c_o:
                            word_list[i] = "O"
                        money += 110
                    else:
                        money -= 10
                else:
                    print("BŁĄD! Masz za mało pieniędzy.")
                    pause()
            else:
                print("BŁĄD! Wybrana litera została wcześniej użyta.")
                pause()
        elif user_vowel_buy_choice == "7" \
        or user_vowel_buy_choice == "Ó" \
        or user_vowel_buy_choice == "ó":
            word_c_ó = [a for a, b in enumerate(word.upper()) if b == "Ó"]
            if "Ó" not in used_letters:
                if money >= 40:
                    money -= 40
                    used_letters.append("Ó")
                    if "Ó" in word.upper():
                        for i in word_c_ó:
                            word_list[i] = "Ó"
                        money += 50
                    else:
                        money -= 10
                else:
                    print("BŁĄD! Masz za mało pieniędzy.")
                    pause()
            else:
                print("BŁĄD! Wybrana litera została wcześniej użyta.")
                pause()
        elif user_vowel_buy_choice == "8" \
        or user_vowel_buy_choice == "U" \
        or user_vowel_buy_choice == "u":
            word_c_u = [a for a, b in enumerate(word.upper()) if b == "U"]
            if "U" not in used_letters:
                if money >= 90:
                    money -= 90
                    used_letters.append("U")
                    if "U" in word.upper():
                        for i in word_c_u:
                            word_list[i] = "U"
                        money += 100
                    else:
                        money -= 10
                else:
                    print("BŁĄD! Masz za mało pieniędzy.")
                    pause()
            else:
                print("BŁĄD! Wybrana litera została wcześniej użyta.")
                pause()
        elif user_vowel_buy_choice == "9" \
        or user_vowel_buy_choice == "Y" \
        or user_vowel_buy_choice == "y":
            word_c_y = [a for a, b in enumerate(word.upper()) if b == "Y"]
            if "Y" not in used_letters:
                if money >= 100:
                    money -= 100
                    used_letters.append("Y")
                    if "Y" in word.upper():
                        for i in word_c_y:
                            word_list[i] = "Y"
                        money += 110
                    else:
                        money -= 10
                else:
                    print("BŁĄD! Masz za mało pieniędzy.")
                    pause()
            else:
                print("BŁĄD! Wybrana litera została wcześniej użyta.")
                pause()
        else:
            pass
    elif user_choice == 3:
        cls()
        print(keyword_guess_message)
        keyword_guess_user_input = input("> ")
        if keyword_guess_user_input == "":
            continue
        if keyword_guess_user_input.upper() == word.upper():
            cls()
            print("GRATULACJE, wygrałeś/aś!")
            print(f"Hasłem było słowo {word.upper()}.")
            print(f"Końcowy budżet: {money} zł.")
            print("")
            print(game_ended_message)
            game_ended_user_choice = 1
            try:
                game_ended_user_choice = int(input("> "))
            except:
                pass
            if game_ended_user_choice == 1:
                cls()
                print("Generowanie nowej gry...")
                delay(2.5)
                generate_word()
                money = 200
            elif game_ended_user_choice == 2:
                quit()
        else:
            print(f'Niestety, "{keyword_guess_user_input}" nie jest \
rozwiązaniem.')
            print("- 50 zł")
            pause()
            money -= 50
    elif user_choice == 4:
        cls()
        print(generate_new_game_message)
        new_game_user_choice = ""
        try:
            new_game_user_choice = int(input("> "))
        except:
            pass
        if new_game_user_choice == 1:
            cls()
            print("Generowanie nowej gry...")
            delay(2.5)
            generate_word()
            money = 200
            used_letters = []
        else:
            pass
    elif user_choice == 5:
        cls()
        print(program_informations)
        print("\n\n")
        pause()
    else:
        pass
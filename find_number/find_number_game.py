import random

def generate_random_number(min_val, max_val):
    """Генеруємо випадкове число"""
    return random.randint(min_val, max_val)

def restart_game():
    """Пропонуємо гравцеві ще раз зіграти в гру."""
    print("Do you wanna play again? (введи 'yes' або 'no')")
    user_answer = input().lower()
    if user_answer == "yes":
        choose_and_play()
    else:
        print("Goodbye!")

def choose_level():
    """Тут користувач обирає рівень, або налаштовує свій власний рівень складності"""
    print(f"Choose your level: 'child', 'easy', 'normal', 'hard', 'dead' if you want set your own level enter 'customize'")
    user_choose_level = input().lower()
    return user_choose_level

def level_parameters(user_choose_level):
    """Передаємо параметри гри"""
    if user_choose_level == 'child':
        return 1, 5, 3
    if user_choose_level == 'easy':
        return 1, 10, 3
    if user_choose_level == 'normal':
        return 1, 25, 3
    if user_choose_level == 'hard':
        return 1, 100, 3
    if user_choose_level == "dead":
        return 1, 1000000, 1
    if user_choose_level == 'customize':
        min_number = int(input("Enter min number: "))
        max_number = int(input("Enter max number: "))
        user_attempts = int(input("Enter attempts: "))
        return min_number, max_number, user_attempts

def play_game(user_choose_level):
    """Запускаємо гру"""
    min_number, max_number, user_attempts = level_parameters(user_choose_level)
    secret_number = generate_random_number(min_number, max_number)

    print(f"Спробуй вгадати число від {min_number} до {max_number}. У тебе є {user_attempts} спроби. Успіхів!")

    for i in range(user_attempts):
        user_input = int(input())
        if user_input == secret_number:
            print("Вітаємо, ви виграли!")
            restart_game()
            return  # Вихід з функції, бо гра закінчилась
        else:
            attempts_left = user_attempts - i - 1
            if attempts_left > 0:
                print(f"Спробуй ще. У тебе залишилось ще: {attempts_left} спроба.")
            else:
                print(f"На жаль ти вичерпав усі проби. Secret number was {secret_number}")
                restart_game()
                return  # Вихід з функції, бо гра закінчилась

def choose_and_play():
    """Гравець обирає рівень і розпочинає гру"""
    user_level = choose_level()
    play_game(user_level)

# Початок гри
choose_and_play()

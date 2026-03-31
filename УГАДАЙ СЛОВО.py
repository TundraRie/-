# Библиотека
from random import *

# Правила
print("Привет!")
print("Попробуй угадать слово по буквам")

# Переменные
words = ["привет",
    "пайтон",
    "учитель",
    "россия",
    "окак"]

word = choice(words)  # Выбор

attempts = 5  # Попытки
user_letters = []

# Зашифровка слова
for i in range(len(word)):
    print("x", end = "")

# Выиграл или проиграл
while True:
    is_win = True
    print(" Попыток: ", attempts)

    user = input("Введите букву: ")  # Ввод юзера
    if user not in user_letters:  # Если не вводил
        user_letters.append(user)
    for letter in word:  # Перебираем
        if letter in user_letters:
            print(letter, end = "")  # Если есть буква
        else:
            print("x", end = "")  # Если нет буквы
            is_win = False
    print()
    if user not in word:
        attempts -= 1
        print("Нету буквы")
    if attempts == 0:
        print("Вы проиграли")
        break
    if is_win == True:
        print("Вы выиграли")
        break

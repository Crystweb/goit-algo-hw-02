# Необхідно розробити функцію, яка приймає рядок як вхідний параметр, додає всі його символи до двосторонньої черги
# (deque з модуля collections в Python), а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок
# паліндромом. Програма повинна правильно враховувати як рядки з парною, так і з непарною кількістю символів, а також
# бути нечутливою до регістру та пробілів.

from collections import deque


def is_palindrome(s: str) -> bool:
    # Привести рядок до нижнього регістру та видалити всі пробіли
    s = ''.join(c.lower() for c in s if c.isalnum())

    # Створити двосторонню чергу
    char_deque = deque(s)

    # Порівнювати символи з обох кінців черги
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True


# Приклади використання
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome("Was it a car or a cat I saw"))  # True
print(is_palindrome("No lemon, no melon"))  # True

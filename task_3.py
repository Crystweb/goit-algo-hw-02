# Напишіть програму, яка читає рядок з послідовністю символів-розділювачів, наприклад, ( ) { [ ] ( ) ( ) { } } },
# і надає відповідне повідомлення, коли розділювачі симетричні, несиметричні, наприклад ( ( ( ) , або коли розділювачі
# різних видів стоять у парі, як-от ( }.

def check_delimiters(expression: str) -> str:
    # Визначаємо пари символів-розділювачів
    open_to_close = {'(': ')', '[': ']', '{': '}'}
    close_to_open = {')': '(', ']': '[', '}': '{'}

    # Стек для зберігання відкритих символів-розділювачів
    stack = []

    for char in expression:
        if char in open_to_close:  # Якщо це відкриваючий символ
            stack.append(char)
        elif char in close_to_open:  # Якщо це закриваючий символ
            if not stack or stack.pop() != close_to_open[char]:
                return "Несиметрично"

    if stack:
        return "Несиметрично"
    else:
        return "Симетрично"


# Приклади використання
print(check_delimiters("( ){[ 1 ]( 1 + 3 )( ){ }}"))  # Симетрично
print(check_delimiters("( 23 ( 2 - 3);"))  # Несиметрично
print(check_delimiters("( 11 }"))  # Несиметрично

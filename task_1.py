# Потрібно розробити програму, яка імітує приймання й обробку заявок: програма має автоматично генерувати нові заявки
# (ідентифіковані унікальним номером або іншими даними), додавати їх до черги, а потім послідовно видаляти з черги
# для "обробки", імітуючи таким чином роботу сервісного центру.

import queue
import threading
import time
import random

# Створити чергу заявок
request_queue = queue.Queue()

# Змінна для унікального ідентифікатора заявок
request_id = 0


def generate_request():
    global request_id
    while True:
        request_id += 1
        request = f"Request_{request_id}"
        print(f"Generating {request}")
        request_queue.put(request)
        time.sleep(random.uniform(0.5, 2))  # Імітуємо випадковий час генерації нових заявок


def process_request():
    while True:
        if not request_queue.empty():
            request = request_queue.get()
            print(f"Processing {request}")
            time.sleep(random.uniform(1, 3))  # Імітуємо час обробки заявки
        else:
            print("Queue is empty, waiting for new requests...")
            time.sleep(1)


# Головний цикл програми з використанням потоків
def main():
    generator_thread = threading.Thread(target=generate_request)
    processor_thread = threading.Thread(target=process_request)

    generator_thread.start()
    processor_thread.start()

    generator_thread.join()
    processor_thread.join()


if __name__ == "__main__":
    main()

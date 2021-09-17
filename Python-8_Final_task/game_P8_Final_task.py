"""Игра угадай число
Компьютер сам загадывает и сам угадывает число меньше чем за 20 попыток
"""

import numpy as np

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    #print(number, end = ', ')
    count = 0
    a = 1
    b = 101

    while True:
        count += 1
        predict_number = np.random.randint(a, b)  # предполагаемое число
        #print(predict_number, end=', ')
        if number > predict_number:
            a = predict_number
        elif number < predict_number:
            b = predict_number
        else:
            break  # выход из цикла если угадали
    #print(count, end=',  ')
    return count

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)

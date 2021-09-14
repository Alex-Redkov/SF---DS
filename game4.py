import numpy as np

def random_predict(number:int=1) -> int:

  count = 0

  while True:
    count += 1
    predict_number = np.random.randint(1, 101) # предполагаемое число
    #print(predict_number, end = ", ")
    if number == predict_number:
        break # выход из цикла, если угадали
  return(count)

#print(f'Количество попыток: {random_predict(10)}')


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для вопроизводимости
    #print(np.random.seed(1))
    random_array = np.random.randint(1, 101, size=(10)) # загадали список чисел
    #print(random_array, end=', ')

    for number in random_array:
        count_ls.append(random_predict(number))
        print(number, end=', ')

    score = int(np.mean(count_ls)) # находим среднее количество попыток
    
    print('\n') 
    print(".....")
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    print(".....")
    print(count_ls)
    return(score)

if __name__ == '__main__':
    score_game(random_predict)
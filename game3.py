import numpy as np

def random_predict(number:int=1) -> int:
    

    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)

if __name__=='__main__':
    #RUN
    print(f'Количество попыток: {random_predict(100)}')
    
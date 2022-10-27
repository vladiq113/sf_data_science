import numpy as np
def random_predict(number) -> int:
    """Компьютер угадывает рандомное число
    Args:
        number (int, optional): Загаданное число.
    Returns:
        int: Число попыток
    """
    predict_number = np.random.randint(1, 101) # загадываем рандомное число, используя генератор рандомных чисел
    count = 0 # Переменная счетчик
    minimum_value = 1 # Минимальное значение рассматриваемого интервала
    maximum_value = 100 # Максимальное значение рассматриваемого интервала
   
    while True:
        count += 1
        if predict_number > number:
            maximum_value = predict_number - 1
            predict_number = (maximum_value + minimum_value) // 2
        elif predict_number < number:
            minimum_value = predict_number + 1
            predict_number = (maximum_value + minimum_value) // 2
        else:
            #print(f'Компьютер угадал загаданное число за {count} попыток. Это число {number}')
            break # конец игры и выход из цикла
    return(count)
# print(f'Количество попыток: {random_predict(number)}')
def score_game(random_predict) -> int:
    """ За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм
    Args:
        random_predict ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попытки')

if __name__ == "__main__":
    # RUN
    score_game(random_predict)
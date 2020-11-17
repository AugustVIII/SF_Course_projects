import numpy as np

def game_core_v3(number):
    '''Сначала устанавливаем половину от длины заданного диапазона, а потом уменьшаем или увеличиваем на половину от
    длины оставшегося диапазона, в зависимости от того, больше оно или меньше нужного. Функция принимает загаданное
    число и возвращает число попыток'''
    count = 1
    len_range = 101 - 1  # длина заданного диапазона, необязательная переменная
    predict = len_range // 2  # первое загаданное число - половина от длины заданного диапазона
    step_predict = predict // 2  # шаг, на который будет увеличиваться или уменьшаться число

    while number != predict:
        count += 1
        if number > predict:
            predict += step_predict
        elif number < predict:
            predict -= step_predict

        if step_predict == 1: # если шаг дошел до 1, то он перестает делиться на 2 без остатка, иначе - бесконечный цикл
            continue
        else:
            step_predict //= 2

    return (count)  # выход из цикла, если угадали


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")

    return (score)

score_game(game_core_v3)
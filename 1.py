import random

def point():
    """Генерация случайной точки в декртовой плоскости (х, у)"""
    return (random.randint(-100, 100), random.randint(-100, 100))

def point_array(n):
    """Функция создает список из n случайных точек на плоскости (х, у)"""
    spisok = []
    for _ in range(n):
        spisok.append(point())
    return spisok

def ctang(g):
    """Функция осуществляет сортировку в зависимости от значчения катангенца"""
    return g[0] / g[1]

def sort_(r):
    """Функция осуществляет сортировку случайных точек в порядке обхода против часовой стрелки,
    начиная с точки наиболее близко лежащей к оси ординат в I координатной четверти """
    chetv_1 = []
    chetv_2 = []
    chetv_3 = []
    chetv_4 = []
    plus = []
    minus = []
    first =[]
    for i in r:
        if (i[0] >= 0) & (i[1] > 0):
            chetv_1.append(i)
            
        elif (i[0] < 0) & (i[1] > 0):
            chetv_2.append(i)
            
        elif (i[0] < 0) & (i[1] < 0):
            chetv_3.append(i)
            
        elif (i[0] > 0) & (i[1] < 0):
            chetv_4.append(i)
        else:
            if (i[0] > 0):
                plus.append(i)
            else:
                minus.append(i) 
        chetv_4.sort(key = ctang)
        chetv_1.sort(key = ctang)
        chetv_2.sort(key = ctang)
        chetv_3.sort(key = ctang)
    if (len(chetv_1) >= 1):
        first.append(chetv_1.pop(0))
    return first + plus + chetv_2 + chetv_3 + minus + chetv_4 + chetv_1

def r_print(n):
    """Функция принимает на вход список из n точек и оттображает полученные точки,
    показывает среднее, минимальное и максимальное расстояние до точек от начала координат"""
    a = sort_(point_array(n))
    lenght = [(i[0]**2 + i[1]**2)**(1 / 2) for i in a]
    print(f'Среднее расстояние: {round(sum(lenght) / len(lenght), 3)}')
    print(f'Минимальное расстояние: {round(min(lenght), 3)}')
    print(f'Максимальное расстояние: {round(max(lenght), 3)}')
    print(f'Точки: {a}')

n = input('Введите количество точек: ')
try:
    r_print(int(n))
except:
    print(f'Ошибка вы ввели {n} вместо целого числа')

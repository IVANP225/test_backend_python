import random

grz = ["A123AA11", "А222АА123", "A12AA123", "A123CC1234", "AA123A12", 'A000CC134',
     'A123AA002', 'A22OEE080', 'O001OO01', 'Q123EE177', 'AA434A23', 'K345KK012']

def try_grz():
    """Генератор ГРЗ типа 1А"""
    letter = ['А', 'В', 'Е', 'К', 'М', 'Н', 'О', 'Р', 'С', 'Т', 'У', 'Х',
             'A', 'B', 'E', 'K', 'M', 'H', 'O', 'P', 'C', 'T', 'Y', 'X']
    first_l = random.randint(0, len(letter) - 1)
    second_l = random.randint(0, len(letter) - 1)
    third_l = random.randint(0, len(letter) - 1)
    digit = str(random.randint(1, 999))
    while (len(digit) < 3):
        digit = '0' + digit   
    region = str(random.randint(1, 999))
    if (len(region) == 1):
        region = '0' + region
    return letter[first_l] + digit + letter[second_l] + letter[third_l] + region

for _ in range(50):
    grz.append(try_grz())


def gos_nomer_rus(g):
    """Проверка корректнсти госсударственного регистрационного знака типа 1А.
        1. проверка необходимой длины
        2. проверка букв в ГРЗ на соответстие и в нужных местах
        3. проверка цифр на соответствие
        4. проверка на соответствие региона
    """
    letter = ['А', 'В', 'Е', 'К', 'М', 'Н', 'О', 'Р', 'С', 'Т', 'У', 'Х',
             'A', 'B', 'E', 'K', 'M', 'H', 'O', 'P', 'C', 'T', 'X']
    true_nomer = []
    for i in g:
        if 8 <= len(i) <= 9:
            if (i[0] in letter) & (i[4] in letter) & (i[5] in letter):
                if (i[1].isdigit()) & (i[2].isdigit()) & (i[3].isdigit())&(i[1:4]!='000'):
                    if ((len(i[6:]) == 3) & (i[6] != '0') | ((len(i[6:]) == 2) & (i[6:] != '00')) & (i[6:].isdigit())):
                        true_nomer.append(i)
    return true_nomer

print(*gos_nomer_rus(grz), sep = '\n')

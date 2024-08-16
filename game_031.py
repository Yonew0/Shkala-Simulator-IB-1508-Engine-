from progress.bar import IncrementalBar
import time
import os
import random
import sys

def bober_kurva(text: str, elements: int, timeout: float):
    with IncrementalBar(text, max=elements) as bar:
        for i in range(elements):
            bar.next()
            time.sleep(timeout)

def russkiy_control():
    dick = {"Б_я_и_на": "блядина", "Х_й": "хуй", "А_ан_с": "ананас"}
    pussy = random.randint(0, 2)
    if pussy == 0:
        inp_l = input(f"Вставьте буквы и напишите результат: Б_я_и_на\n")
        if (inp_l.lower() == f"{dick['Б_я_и_на']}"):
            print("Вы решили контрольную! Продолжаем.")
        else:
            print("[Змеюка] ПАЗОРИЩИ!!!! НИВЕРНА!!!!!")
            return 1
    elif pussy == 1:
        inp_l = input(f"Вставьте буквы и напишите результат: Х_й\n")
        if (inp_l.lower() == f"{dick['Х_й']}"):
            print("Вы решили контрольную! Пpодолжаем.")
        else:
            print("[Змеюка] ПАЗОРИЩИ!!!! НИВЕРНА!!!!!")
            return 1
    elif pussy == 2:
        inp_l = input(f"Вставьте буквы и напишите результат: А_ан_с\n")
        if (inp_l.lower() == f"{dick['А_ан_с']}"):
            print("Вы решили контрольную! Продолжаем.")
        else:
            print("[Змеюка] ПАЗОРИЩИ!!!! НИВЕРНА!!!!!")
            return 1

def litra_control():
    inp_l = input(f"Как звали Глиста А.С Пушкина?\n")
    if (inp_l.lower() == f"олег"):
        print("Вы решили контрольную! Продолжаем.")
    else:
        print("[Змеюка] ПАЗОРИЩИ!!!! НИВЕРНА!!!!!")
        return 1


print('''
Добро пожаловать в игру "Симулятор ШКАЛЫ"
Версия 0.03 (For RedHat GNU\Linux)''')

bober_kurva("Загрузка ресурсов", 10, timeout=0.5)
bober_kurva("Загрузка диалогов", 10, timeout=0.5)

print("Вы опоздали на Урок")

inp = input("[Змеюка] Почему опоздал : ")
print(f"{inp}, значит. Я в сказки не верю садись")

while True:
    inp = input("Введите [Ф] чтобы сесть на стул : ")
    if inp.lower() == 'ф':
        bober_kurva("Сесть на стул", 5, 0.5)
        break

print("\n")
print("Урок русского языка... Что может быть хуже?")

while True:
    inp = input("Что вы хотите сделать? (Для справки введите 'помощь') > ")
    match inp:
        case "помощь":
            print("Возможные действия: бежать, решать, пукнуть")
        case "бежать":
            rand = random.randint(0, 100)
            bober_kurva("Попытка бежать", 20, timeout=0.5)
            if rand <= 10:
                print('''
Вы сбежали из "тюрьмы", пробежав мимо охраны, и перепрыгнув забор,
вдыхаете свежий воздух свободы - и бежите куда глаза глядят...
[Вы] Наконец-то! Получилось''')
                input()
                sys.exit()
                break
            else:
                print("Вас поймали и вернули в класс.")
        case "решать":
            if russkiy_control() != 1:
                break
        case "пукнуть":
            rand = random.randint(0, 100)
            bober_kurva("Попытка пукнуть", 6, 0.5)
            if rand <= 15:
                print("[Змеюка] ОНЕТ ЭТА ГАЗАВЫЪИ АТАКИ! ЪА УМИРАЪУ!")
                print('''
Вы сбежали из "тюрьмы", пробежав мимо охраны, и перепрыгнув забор,
вдыхаете свежий воздух свободы - и бежите куда глаза глядят...
[Вы] Наконец-то! Получилось''')
                input()
                sys.exit()
            else:
                print("Змеюка пристыдила вас, и вы чуть-ли не умерли от стыда.")

print("\nЛитра... Лучше уж помереть...")
while True:
    inp = input("Что вы хотите сделать? (Для справки введите 'помощь') > ")
    match inp:
        case "помощь":
            print("Возможные действия: бежать, решать, пукнуть")
        case "бежать":
            rand = random.randint(0, 100)
            bober_kurva("Попытка бежать", 20, timeout=0.5)
            if rand <= 10:
                print('''
Вы сбежали из "тюрьмы", пробежав мимо охраны, и перепрыгнув забор,
вдыхаете свежий воздух свободы - и бежите куда глаза глядят...
[Вы] Наконец-то! Получилось''')
                input()
                sys.exit()
                break
            else:
                print("Вас поймали и вернули в класс.")
        case "решать":
            if litra_control() != 1:
                break
        case "пукнуть":
            rand = random.randint(0, 100)
            bober_kurva("Попытка пукнуть", 6, 0.5)
            if rand <= 15:
                print("[Змеюка] ОНЕТ ЭТА ГАЗАВЫЪИ АТАКИ! ЪА УМИРАЪУ!")
                print('''
Вы сбежали из "тюрьмы", пробежав мимо охраны, и перепрыгнув забор,
вдыхаете свежий воздух свободы - и бежите куда глаза глядят...
[Вы] Наконец-то! Получилось''')
                input()
                sys.exit()
            else:
                print("Змеюка пристыдила вас, и вы чуть-ли не умерли от стыда.")
print("Вы так и не решились бежать, и вы умерли от скуки на следующем уроке ТРУДОБЛУДИИ")
print('''
Thanks for playing IB-1508!
Copyright, VAND INC''')
input()

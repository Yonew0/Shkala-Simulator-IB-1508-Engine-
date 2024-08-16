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

def trudobludia_dlc():
    while True:
        print("[Хриплая Училка] Быстро лепи ЭЛФЕФУ БАШНИ из фанеры!\nВ МАСШТАБЕ 1:1")
        inp_l = input("Действие (для справки введите 'помощь') > ")
        match inp_l.lower():
            case "помощь":
                print("Возможные действия: смастерить, пукнуть, обусждать с другом")
            case "смастерить":
                bober_kurva("Попытка смастерить", 6, 0.5)
                rand = random.randint(0, 100)
                if rand <= 50:
                    print("У вас соскачил лобзик\n[Хриплая Училка] ОТВРАТИТИЛЬНА!!! ПЕРЕДЕЛЫВАЙ ПИДОРАС")
                else:
                    print("Вы успешно смастерили элфеву башню")
                    break
            case "пукнуть":
                rand = random.randint(0, 100)
                bober_kurva("Попытка пукнуть", 6, 0.5)
                if rand <= 15:
                    print("[Хриплая Училка] ОНЕТ ЭТА ГАЗАВЫЪИ АТАКИ! ЪА УМИРАЪУ!")
                    print('''
Вы сбежали из "тюрьмы", пробежав мимо охраны, и перепрыгнув забор,
вдыхаете свежий воздух свободы - и бежите куда глаза глядят...
[Вы] Наконец-то! Получилось''')
                    input()
                    sys.exit()
                else:
                    print("Хриплая Училка пристыдила вас, и вы чуть-ли не умерли от стыда.")
            case "обсуждать с другом":
                bober_kurva("Вы обсуждаете побег с Другом", 10, 0.8)
                rand = random.randint(0, 100)
                if rand <= 5:
                    print("""
Вы с другом придумали идеальный план побега, и сбежали через окно
Вдохнув воздуха свободы, вы купили себе мороженое""")
                    sys.exit()
                    break
                else:
                    print("[Хриплая Училка] ЧТО ВЫ ТАМ ШУШУКАЪЕТЕСЪ РАКИ?")
                    print("Вас обосрали.")

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

def lesson(lesson_control):
    while True:
        inp_la = input("Что вы хотите сделать? (Для справки введите 'помощь') > ")
        match inp_la:
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
                if lesson_control() != 1:
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

lesson(russkiy_control)

print("\n")
print("\nЛитра... Лучше уж помереть...")

lesson(litra_control)

print("\n")
print("Трудоблудия... Умереть - будет лучше")
trudobludia_dlc()

print("Вы так и не решаете бежать, и умерли от скуки на уроке ТАМИСЯМИКИ")

print('''
Thanks for playing IB-1508!
Copyright, VAND INC''')
input()

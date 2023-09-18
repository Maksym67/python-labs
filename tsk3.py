import time
import random

def delay_print(text):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(random.random() * 0.06)
    print()

def ariOper(opernum1, opernum2):
    delay_print('\n1. Додавання.\n2. Віднімання.\n3. Множення.\n4. Ділення.')
    selectedOper = int(input("\nВиберіть дію (1-4): "))

    res = None

    if selectedOper == 1:
        res = opernum1 + opernum2
    elif selectedOper == 2:
        res = opernum1 - opernum2
    elif selectedOper == 3:
        res = opernum1 * opernum2
    elif selectedOper == 4:
        res = opernum1 / opernum2
    else:
        delay_print("Вибрана невірна дія!")

    delay_print(f"Результат: {res}")

def compNum(opernum1, opernum2):
    if opernum1 == opernum2:
        delay_print('\nЧисла рівні.')
    elif opernum1 > opernum2:
        delay_print(f'\nЧисло {opernum1} більше за число {opernum2}')
    elif opernum1 < opernum2:
        delay_print(f'\nЧисло {opernum1} менше за число {opernum2}')
    else:
        delay_print('\nПомилка.')

def typeChng(opernum1, opernum2):
    delay_print('\n1. Integer.\n2. Float.')
    selectedOper = int(input("Виберіть тип для заміни: "))

    if selectedOper == 1:
        resNum1 = int(opernum1)
        resNum2 = int(opernum2)
    elif selectedOper == 2:
        resNum1 = float(opernum1)
        resNum2 = float(opernum2)
    else:
        delay_print('Вибрана невірна дія!')

    delay_print(f"Результат:  \nчисло 1: {resNum1}, \nчисло 2: {resNum2}")

num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))

delay_print('\n1. Арифметичні операції.\n2. Порівняння.\n3. Перетворення типів даних.')

selectedOpt = int(input('\nВиберіть дію (1-3): '))

if selectedOpt == 1:
    ariOper(num1, num2)
elif selectedOpt == 2:
    compNum(num1, num2)
elif selectedOpt == 3:
    typeChng(num1, num2)
else:
    delay_print('Вибрана невірна дія!')
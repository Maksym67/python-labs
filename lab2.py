import time
import random

def delay_print(s):
    for c in s:
        print(c, end='',  flush=True)
        time.sleep(random.random() * 0.01)
    print()

character_name = input("Вітаю! Введіть ім'я вашого персонажа: ")
delay_print("Вітаю, " + character_name + "! Тобі належить вибрати свій шлях у невеликій грі, в результаті якої ти дізнаєшся який сік компанії Січко™ тобі підходить найбільше!")

answers_array = []
quest_index = 0

delay_print("Вітаю на першому рівні! До тебе підходить невідоме створіння, схоже на гнома, і каже:\n'Привіт, незнайомцю. Якщо ти хочеш пройти, то тобі потрібно відгадати загадку. Якщо ти не хочеш, то я тебе вб'ю.'")

print("\nВаріанти відповідей:\n1) 'Так, я хочу відгадати загадку.'\n2) 'Ні, я не хочу відгадувати загадку. (почати драку)'")

answer = input("Введіть відповідь: ")
answers_array.append(answer)

if answer == "1":
    delay_print("\nГном: 'Добре, тоді почнемо. Якщо ти відгадаєш, то я тобі дам піти.'")
elif answer == "2":
    delay_print("\nГном: 'Ти вирішив битися? Тоді почнемо.'")
else:
    delay_print("Гном: 'Я не розумію тебе. Якщо ти не зможеш відповісти, то я тебе вб'ю.'")

quest_index = 1
previous_answer = answers_array[quest_index - 1]

if previous_answer == "1":
    delay_print("Гном: 'У мами Івана було три сини. Першого звали Петро, другого – Василь. Як звали третього сина?'")
    print("\nВаріанти відповідей:\n1) 'Іван'\n2) 'Петро'\n3) 'Василь'")
    answer = input("Введіть відповідь: ")
    answers_array.append(answer)
elif previous_answer == '2':
    print("*Гном розмахується кулаком і ударяє вас по коліну.*")
    delay_print("Гном: 'Н-Н-Н-А-А-А!!!'")
    print("*Ви відчуваєте сильний біль в коліні але він не надто сильний*")
    print("1. *вдарити гнома з усієї сили ногою*\n2. Будь ласка!!! Не бий! Я відповім на твою загадку!!!")
    answer = input("Введіть відповідь: ")
    answers_array.append(answer)
else:
    delay_print("Гном: 'Шо ти там бормочеш??!!'")

quest_index = 2
previous_answer = answers_array[quest_index - 1]

if previous_answer == "1":
    delay_print("Гном: 'Відповідь правильна! Ти можеш іти далі.'")
    print("*Гном відступає, відкриваючи шлях глибше в ліс.*")
elif previous_answer == '2':
    print("*Ви виграваєте гнома пнуттям, і він впадає, обурений.*")
    delay_print("Гном: 'Ти виявився сильнішим, але це ще не кінець.'")
    print("*Гном встає і відкриває шлях глибше в ліс.*")
else:
    delay_print("Гном: 'Шо ти там бормочеш??!!'")

print("\nВи вибрали такі відповіді:")
for i, answer in enumerate(answers_array):
    print(f"{i + 1}: {answer}")

delay_print("\nГра завершилася. Дякуємо за участь, " + character_name + "!")
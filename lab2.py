import time
import random

def delay_print(s):
    for c in s:
        print(c, end='',  flush=True)
        time.sleep(random.random() * 0.01)
    print()

character_name = input("Вітаю! Введіть ім'я вашого персонажа: ")

delay_print("Вітаю, " + character_name + "! Тобі належить вибрати свій шлях у невеликій грі, в результаті якої ти дізнаєшся закінчення захоплюючого сюжету!")

answers_array = []
quest_index = 0

delay_print("Вітаю на першому рівні! До тебе підходить невідоме створіння, схоже на гнома, і каже:\n'Привіт, незнайомцю. Якщо ти хочеш пройти, то тобі потрібно відгадати загадку. Якщо ти не хочеш, то я тебе вб'ю.'")
print("\nВаріанти відповідей:\n1) 'Так, я хочу відгадати загадку.'\n2) 'Ні, я не хочу відгадувати загадку. (почати бійку)'")

answer = input("Введіть відповідь: ")
answers_array.append(answer)

previous_answer = answers_array[0]

if (previous_answer == "1"):
    delay_print("\nГном: 'Добре, тоді почнемо. Якщо ти відгадаєш, то я тобі дам піти.'")
elif (previous_answer == "2"):
    delay_print("\nГном: 'Ти вирішив битися? Тоді почнемо.'")
else:
    delay_print("Гном: 'Я не розумію тебе. Якщо ти не зможеш відповісти, то я тебе вб'ю.'")

if (previous_answer == "1"):
    delay_print("Гном: 'У мами Івана було три сини. Першого звали Петро, другого – Василь. Як звали третього сина?'")
    print("Варіанти відповідей:\n1) Іван.\n2) Василь.\n3) Петро.")
    answer = input("Відповідь: ")
    answers_array.append(answer)

    previous_answer = answers_array[1]

    if (previous_answer == "1"):
        delay_print("Молодець! Тепер ти можеш йти.\nВиберіть куди підете:\n1) Додому.\n2) В кіно.\n3) В театр.")
        answer = input("Відповідь: ")
        answers_array.append(answer)

        previous_answer = answers_array[2]

        if(previous_answer == "1"):
            print("Гном: 'Ми ще зустрінемось!'")
        elif(previous_answer == "2"):
            print("Гном: 'Рекомендую піти на фільм 'Людина-павук', нова частина вже в прокаті.'")
        elif(previous_answer == "3"):
            print("Гном: 'Краще б пішов у кіно!'")
        else:
            quit()

    elif(previous_answer == "2"):
        delay_print("Гном: Неправильно! Але я дам тобі другий шанс! Що можна утримувати, не торкаючись його руками?\nВаріанти відповідей:\n1) Дихання.\n2) Гроші.\n3) Воду.")
        answer = input("Відповідь: ")
        answers_array.append(answer)

        previous_answer = answers_array[2]

        if(previous_answer == "1"):
            delay_print("Молодець! Тепер ти можеш йти.\nВиберіть куди підете:\n1) Додому.\n2) В кіно.\n3) В театр.")
            answer = input("Відповідь: ")
            answers_array.append(answer)

            previous_answer = answers_array[3]

            if(previous_answer == "1"):
                print("Гном: 'Ми ще зустрінемось!'")
            elif(previous_answer == "2"):
                print("Гном: 'Рекомендую піти на фільм 'Людина-павук', нова частина вже в прокаті.'")
            elif(previous_answer == "3"):
                print("Гном: 'Краще б пішов у кіно!'")
            else:
                quit()

        elif(previous_answer == "2"):
            delay_print("Знову неправильно! Спробуємо останній раз. Що не жує, але все пожирає?\nВаріанти відповіді:\n1) Вогонь.\n2) Вода.\n3) Вітер.")
            answer = input("Відповідь: ")
            answers_array.append(answer)

            previous_answer = answers_array[3]

            if(previous_answer == "1"):
                delay_print("Молодець! Тепер ти можеш йти.\nВиберіть куди підете:\n1) Додому.\n2) В кіно.\n3) В театр.")
                answer = input("Відповідь: ")
                answers_array.append(answer)

                previous_answer = answers_array[4]

                if(previous_answer == "1"):
                    print("Гном: 'Ми ще зустрінемось!'")
                elif(previous_answer == "2"):
                    print("Гном: 'Рекомендую піти на фільм 'Людина-павук', нова частина вже в прокаті.'")
                elif(previous_answer == "3"):
                    print("Гном: 'Краще б пішов у кіно!'")
                else:
                    quit()
            elif(previous_answer == "2"):
                print("You died. The end.")
            elif(previous_answer == "3"):
                print("You died. The end.")

    elif(previous_answer == "3"):
        delay_print("Гном: Неправильно! Але я дам тобі другий шанс! Що можна утримувати, не торкаючись його руками?\nВаріанти відповідей:\n1) Дихання.\n2) Гроші.\n3) Воду.")
        answer = input("Відповідь: ")
        answers_array.append(answer)

        previous_answer = answers_array[2]

        if(previous_answer == "1"):
            delay_print("Молодець! Тепер ти можеш йти.\nВиберіть куди підете:\n1) Додому.\n2) В кіно.\n3) В театр.")
            answer = input("Відповідь: ")
            answers_array.append(answer)

            previous_answer = answers_array[3]

            if(previous_answer == "1"):
                print("Гном: 'Ми ще зустрінемось!'")
            elif(previous_answer == "2"):
                print("Гном: 'Рекомендую піти на фільм 'Людина-павук', нова частина вже в прокаті.'")
            elif(previous_answer == "3"):
                print("Гном: 'Краще б пішов у кіно!'")
            else:
                quit()

        elif(previous_answer == "2"):
            delay_print("Знову неправильно! Спробуємо останній раз. Що не жує, але все пожирає?\nВаріанти відповіді:\n1) Вогонь.\n2) Вода.\n3) Вітер.")
            answer = input("Відповідь: ")
            answers_array.append(answer)

            previous_answer = answers_array[3]

            if(previous_answer == "1"):
                delay_print("Молодець! Тепер ти можеш йти.\nВиберіть куди підете:\n1) Додому.\n2) В кіно.\n3) В театр.")
                answer = input("Відповідь: ")
                answers_array.append(answer)

                previous_answer = answers_array[4]

                if(previous_answer == "1"):
                    print("Гном: 'Ми ще зустрінемось!'")
                elif(previous_answer == "2"):
                    print("Гном: 'Рекомендую піти на фільм 'Людина-павук', нова частина вже в прокаті.'")
                elif(previous_answer == "3"):
                    print("Гном: 'Краще б пішов у кіно!'")
                else:
                    quit()
            elif(previous_answer == "2"):
                print("You died. The end.")
            elif(previous_answer == "3"):
                print("You died. The end.")

elif(previous_answer == "2"):
    delay_print("Ви почали бійку з Гномом. Виберіть наступну дію:")
    print("\n1) Добре, я відгадаю твої загадки.\n2) Вдарити Гнома з усієї сили.")

    answer = input("Відповідь: ")
    answers_array.append(answer)

    previous_answer = answers_array[1]

    if(previous_answer == "1"):

        delay_print("Гном: 'У мами Івана було три сини. Першого звали Петро, другого – Василь. Як звали третього сина?'")
        print("Варіанти відповідей:\n1) Іван.\n2) Василь.\n3) Петро.")
        answer = input("Відповідь: ")
        answers_array.append(answer)

        previous_answer = answers_array[1]

        if (previous_answer == "1"):
            delay_print("Молодець! Тепер ти можеш йти.\nВиберіть куди підете:\n1) Додому.\n2) В кіно.\n3) В театр.")
            answer = input("Відповідь: ")
            answers_array.append(answer)

            previous_answer = answers_array[2]

            if(previous_answer == "1"):
                print("Гном: 'Ми ще зустрінемось!'")
            elif(previous_answer == "2"):
                print("Гном: 'Рекомендую піти на фільм 'Людина-павук', нова частина вже в прокаті.'")
            elif(previous_answer == "3"):
                print("Гном: 'Краще б пішов у кіно!'")
            else:
                quit()

        elif(previous_answer == "2"):
            delay_print("Гном: Неправильно! Але я дам тобі другий шанс! Що можна утримувати, не торкаючись його руками?\nВаріанти відповідей:\n1) Дихання.\n2) Гроші.\n3) Воду.")
            answer = input("Відповідь: ")
            answers_array.append(answer)
    
            previous_answer = answers_array[2]
    
            if(previous_answer == "1"):
                delay_print("Молодець! Тепер ти можеш йти.\nВиберіть куди підете:\n1) Додому.\n2) В кіно.\n3) В театр.")
                answer = input("Відповідь: ")
                answers_array.append(answer)
    
                previous_answer = answers_array[3]
    
                if(previous_answer == "1"):
                    print("Гном: 'Ми ще зустрінемось!'")
                elif(previous_answer == "2"):
                    print("Гном: 'Рекомендую піти на фільм 'Людина-павук', нова частина вже в прокаті.'")
                elif(previous_answer == "3"):
                    print("Гном: 'Краще б пішов у кіно!'")
                else:
                    quit()
    
            elif(previous_answer == "2"):
                delay_print("Знову неправильно! Спробуємо останній раз. Що не жує, але все пожирає?\nВаріанти відповіді:\n1) Вогонь.\n2) Вода.\n3) Вітер.")
                answer = input("Відповідь: ")
                answers_array.append(answer)
    
                previous_answer = answers_array[3]
    
                if(previous_answer == "1"):
                    delay_print("Молодець! Тепер ти можеш йти.\nВиберіть куди підете:\n1) Додому.\n2) В кіно.\n3) В театр.")
                    answer = input("Відповідь: ")
                    answers_array.append(answer)
    
                    previous_answer = answers_array[4]
    
                    if(previous_answer == "1"):
                        print("Гном: 'Ми ще зустрінемось!'")
                    elif(previous_answer == "2"):
                        print("Гном: 'Рекомендую піти на фільм 'Людина-павук', нова частина вже в прокаті.'")
                    elif(previous_answer == "3"):
                        print("Гном: 'Краще б пішов у кіно!'")
                    else:
                        quit()
                elif(previous_answer == "2"):
                    print("You died. The end.")
                elif(previous_answer == "3"):
                    print("You died. The end.")
    
        elif(previous_answer == "3"):
            delay_print("Гном: Неправильно! Але я дам тобі другий шанс! Що можна утримувати, не торкаючись його руками?\nВаріанти відповідей:\n1) Дихання.\n2) Гроші.\n3) Воду.")
            answer = input("Відповідь: ")
            answers_array.append(answer)

            previous_answer = answers_array[2]

            if(previous_answer == "1"):
                delay_print("Молодець! Тепер ти можеш йти.\nВиберіть куди підете:\n1) Додому.\n2) В кіно.\n3) В театр.")
                answer = input("Відповідь: ")
                answers_array.append(answer)

                previous_answer = answers_array[3]

                if(previous_answer == "1"):
                    print("Гном: 'Ми ще зустрінемось!'")
                elif(previous_answer == "2"):
                    print("Гном: 'Рекомендую піти на фільм 'Людина-павук', нова частина вже в прокаті.'")
                elif(previous_answer == "3"):
                    print("Гном: 'Краще б пішов у кіно!'")
                else:
                    quit()

            elif(previous_answer == "2"):
                delay_print("Знову неправильно! Спробуємо останній раз. Що не жує, але все пожирає?\nВаріанти відповіді:\n1) Вогонь.\n2) Вода.\n3) Вітер.")
                answer = input("Відповідь: ")
                answers_array.append(answer)
        
                previous_answer = answers_array[3]
        
                if(previous_answer == "1"):
                    delay_print("Молодець! Тепер ти можеш йти.\nВиберіть куди підете:\n1) Додому.\n2) В кіно.\n3) В театр.")
                    answer = input("Відповідь: ")
                    answers_array.append(answer)
        
                    previous_answer = answers_array[4]
        
                    if(previous_answer == "1"):
                        print("Гном: 'Ми ще зустрінемось!'")
                    elif(previous_answer == "2"):
                        print("Гном: 'Рекомендую піти на фільм 'Людина-павук', нова частина вже в прокаті.'")
                    elif(previous_answer == "3"):
                        print("Гном: 'Краще б пішов у кіно!'")
                    else:
                        quit()

                elif(previous_answer == "2"):
                    print("You died. The end.")
                elif(previous_answer == "3"):
                    print("You died. The end.")
    
else:
    delay_print("Ви застосували суперсилу і вбили гнома!")

print("\nВи вибрали такі відповіді:")
for i, answer in enumerate(answers_array):
    print(f"{i + 1}: {answer}")

delay_print("\nГра завершилася. Дякуємо за участь, " + character_name + "!")
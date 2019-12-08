from time import sleep
from random import randint,choice
from timeit import default_timer
import os

def warnings():
    warnings = ['ты не прав', 'ты хорошо подумал?', 'Неправильно', 'Одумайся']
    return warnings[randint(0, len(warnings)-1)]



def time_endings(digit):
    digit = str(digit)
    last_digit = digit[-1]
    if digit == '11':
        return ''
    else:
        if last_digit == '1':
            return 'у'
        elif 1 < int(last_digit) < 5:
            return 'ы'
        else:
            return ''


def time_convert(time_in_seconds):
    if time_in_seconds < 60:
        time_spent = f'{time_in_seconds} секунд{time_endings(time_in_seconds)}'
    else:
        minutes = time_in_seconds // 60
        seconds = time_in_seconds - (minutes*60)
        if seconds == 0:
            time_spent = f'{minutes} минут{time_endings(minutes)}'
        else:
            time_spent = f'{minutes} минут{time_endings(minutes)} и {seconds} секунд{time_endings(seconds)}'

    return time_spent


def select_mode():
    mode = ''
    if os.path.exists(file_name):
        print('''Режим:
        1 - тренировка
        2 - работ над ошибками''')
    else:
        print('''Режим:
        1 - тренировка
        ''')

    while not mode.isdigit():

        print('Выбери режим')
        mode = input()
        while not mode.isdigit():
            print('Должна быть цифра')
            mode = input()
    return mode

def delete_same_rows():
    uniques = []
    with open(file_name, 'r') as f, open(f'tmp_{file_name}', 'a') as f2:

        for row in f:
            splited = row.split()
            number1, sign, number2, repeat = splited
            unique = f'{number1} {sign} {number2}'
            if unique not in uniques:
                uniques.append(unique)

                f2.write(f'{unique} {repeat}')
                os.delete(file_name)
                os.rename(f'tmp_(file_name)', file_name)




def count():
    print('''Давай проверим твои знания в математике''')

    question_quantity = ''
    count_to = ''
    correct_answers = 0
    fails = 0
    time_in_seconds = 0

    while not question_quantity.isdigit():
        print(name + ', сколько примеров ты готов решить?')
        question_quantity = input()

        if question_quantity.isdigit():
            while int(question_quantity) < 1:
                print('Должно быть больше "0" ')
                question_quantity = input()
                while not question_quantity.isdigit():
                    print('Должна быть цифра!!!')
                    question_quantity = input()
        else:
            print('Должна быть цифра')
    

    while not count_to.isdigit():
        print('До скольки будем считать? Например до 100')
        count_to = input()

        if count_to.isdigit():
            while int(count_to) < 2:
                print('Должно быть больше "1" ')
                count_to = input()
                while not count_to.isdigit():
                    print('Должна быть цифра!!!')
                    count_to = input()

    print('Хорошо, тогда начнем...')
    sleep(1)

    for question in range (int(question_quantity)):
        print(f'Пример {question+1}:')
        number1 = randint(1,int(count_to))
        number2 = randint(1,int(count_to))
        sign = choice('+-')

        if sign == '-':
            while number1 < number2:
                number1 = randint(1, int(count_to))
                number2 = randint(1, int(count_to))
            correct_answer = number1 - number2

        if sign == '+':
            while number1 + number2 > int(count_to):
                number1 = randint(1, int(count_to))
                number2 = randint(1, int(count_to))
            correct_answer = number1 + number2

        print(number1, sign, number2)
        print('Итак, дай свой ответ:')

        start = default_timer()
        student_answer = input()
        stop = default_timer()

        time_in_seconds += round(stop - start)

        if int(student_answer) == correct_answer:
            print('Правильно, молодец')
            correct_answers += 1
        else:
            print(warnings())
            print(f'Правильный ответ: {correct_answer}')
            fails += 1
            with open(file_name, 'a') as f:
                f.write(f'{number1} {sign} {number2} 3\n')

    if fails == 0:
        print(f'Молодец, {name}, ты верно ответил на все вопросы за {time_convert(time_in_seconds)}')
    else:
        print(f'Ошибок {fails}, а правильных ответов {correct_answers}')
        print(f'Затраченное время: {time_convert(time_in_seconds)}')



def fix_errors():
    print(f'{name} Давай исправим твои ошибки')
    file_name2 = f'tmp_{file_name}'

    with open(file_name, 'r') as f:

        line = f.readline()
        splited_line = line.split()
        number1, sign, number2, try_count = splited_line

        print(f'Сколько будет {number1} {sign} {number2}? ')
        answer = input()
        if sign == '-':
            correct_answer = int(number1) - int(number2)
        if sign == '+':
            correct_answer = int(number1) + int(number2)

        with open(file_name2, 'a') as f2:
            if int(answer) == correct_answer:
                print('Молодец')

                f2.write(f'{number1} {sign} {number2} {int(try_count)}-1')
            else:
                print(warnings())





# основной блок программы
print('Привет меня зовут Роджер, а как тебя?')
name = input()
print('Приятно познакомиться ' + name)
count_again = 'да'
file_name = f'{name.lower()}_errors.txt'




while True:

    mode = select_mode()

    if mode == '1':
        count()
    elif mode == '2':
        fix_errors()
    else:
        pass


print('Пока')

from time import sleep
from random import randint, choice
print('Привет! Меня зовут Роджер. А как тебя?')
name = input()
print('приятно познакомиться, ' + name)
print('''Давай проверим твои знания в математике. 
Ты готов? Ответь да или нет?''')
answer = input()
while answer not in {'да', 'нет'}:
    print('Должно быть да или нет.')
    answer = input()
if answer == 'да':

    question_quanitity = ''  # колличество вопросов
    count_to = ''  # до скольки будем считать


    while not question_quanitity.isdigit():
        print(name + ', сколько примеров ты готов решить')
        question_quanitity = input()

        if question_quanitity.isdigit():
            while int(question_quanitity) < 1:
                print('Должно быть больше 0')
                question_quanitity = input()
                while not question_quanitity.isdigit():
                    print('Должна быть цифра')
                    question_quanitity = input()
        else:
            print('Должна быть цифра')

    while not count_to.isdigit():
        print(name + ', До скольки будем считать?')
        count_to = input()

        if count_to.isdigit():
            while int(count_to) < 1:
                print('Должно быть больше 0')
                count_to = input()
                while not count_to.isdigit():
                    print('Должна быть цифра')
                    count_to = input()
        else:
            print('Должна быть цифра')

    print('Хорошо, тогда начинаем...')
    sleep(1)
    for question in  range (int (question_quanitity)):
        print(f'Пример {question+1}:')
        number1 = randint(1, int(count_to))
        number2 = randint(1, int(count_to))
        sign = choice('+-')

        if sign == '-':
            while number1 < number2:
                number1 = randint(1, int(count_to))
                number2 = randint(1, int(count_to))

        if sign == '+':
                while number1 + number2 > int(count_to):
                    number1 = randint(1, int(count_to))
                    number2 = randint(1, int(count_to))

        print(number1, sign, number2)




else:
    print('''Передумал? Хорошо, может как-нибудь в следующий раз..''')

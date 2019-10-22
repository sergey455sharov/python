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

    question_quanitity = ''
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
print('')




else:
    print('''Передумал? Хорошо, может как-нибудь в следующий раз..''')

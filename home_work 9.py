#Створимо порожню телефону книгу, в якій будемо зберігати імена та номери телефону:
TELEPHONEBOOK = {}

#Створимо декоратор для функцій, який буде відлавлювати помилки при введені команд і повертати команди в консоль для їх виправлення:
def  input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except KeyError:
            return 'Give me your name for TELEPHONEBOOK, please!'
        except IndexError:
            return 'Give me your name and telephone, please!'
        except ValueError:
            return 'Cive me correction information, please!'
    return inner




#Напишемо функцію, яка буде зберігати контакти у словник і задекоруємо її:
@input_error
def handler_add(comand:list):
    name = comand[0].title()
    telephone = comand[1]
    TELEPHONEBOOK[name] = telephone
    return f'You successfully added contacts'

#Напишемо функцію, яка буде зберігати новий номер телефону вже існуючого контакту і задекоруємо її:
@input_error
def handler_change(comand:list):
    name = comand[0].title()
    telephone = comand[1]
    if name in TELEPHONEBOOK:
        TELEPHONEBOOK[name] = telephone
        return f'Your telephone was change'
    else:
        return f'Sorry, your name {name} is doesn\'t exist'

#Напишемо функцію, яка виводить у консоль номер телефону по імені, яке вказав користувач і задекоруємо її:
@input_error
def handler_phone(comand):
    if name in TELEPHONEBOOK:
        name = comand[0].title()
        telephone = TELEPHONEBOOK[name]
        return f'Your contact {name} is {telephone}'
    else:
        return f'Sorry, your name {name} is doesn\'t exist'

#Напишемо функцію, яка буде виводити всі збережені дані у консоль
def handler_show_all(*args):
    if TELEPHONEBOOK:
        all_contacts = 'List of contacts\n'
        for name, phone in TELEPHONEBOOK.items():
            all_contacts += f'{name}: {phone}\n'
        return all_contacts
    else:
        return f'Sorry, not contacts in Telephonebook'

#Напишемо функцію, яка буде вітатись:
def handler_hello(*args):
    return f'Helo, can I help you?'

#Створимо словник, який буде співставляти наші функції і команди, які вводе користувач:
COMMANDS = {
    'hello': handler_hello,
    'add': handler_add,
    'change': handler_change,
    'phone': handler_phone,
    'show_all': handler_show_all
}


#Створимо функцію, яка буде розбирати команди, виділяти ключові слова і викликати потрібну нам функцію:
def parser(user_comand):
    user_comand = user_comand.split()
    for key, func in COMMANDS.items():
        if user_comand[0].lower() in key:
            return func(user_comand[1:])

#Створимо головну функцію, яка буде просити у користувача ввести інформацію:
def main():
    exit_words = ['good bye', 'bye', 'close', 'thank you', 'exit']
    while True:
        user_input = input('>>> ' )
        if user_input in exit_words:
            break
        else:
            result = parser(user_input)
            print(result)



if __name__=='__main__':
    main()

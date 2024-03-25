import json

TELEPHONEBOOK_FILE = 'telephonebook.json'

def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except KeyError:
            return 'Give me your name for TELEPHONEBOOK, please!'
        except IndexError:
            return 'Give me your name and telephone, please!'
        except ValueError:
            return 'Give me correct information, please!'
    return inner

# Збереження в файл та завантаження з файлу
def save_to_file():
    with open(TELEPHONEBOOK_FILE, 'w') as file:
        json.dump(TELEPHONEBOOK, file)

def load_from_file():
    try:
        with open(TELEPHONEBOOK_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Оголошення TELEPHONEBOOK та завантаження збережених даних при старті програми
TELEPHONEBOOK = {}
TELEPHONEBOOK.update(load_from_file())

# Додавання контакту
@input_error
def handler_add(command):
    name = command[0].title()
    telephone = command[1]
    TELEPHONEBOOK[name] = telephone
    save_to_file()
    return f'You successfully added contacts'

# Зміна телефонного номера існуючого контакту
@input_error
def handler_change(command):
    name = command[0].title()
    telephone = command[1]
    if name in TELEPHONEBOOK:
        TELEPHONEBOOK[name] = telephone
        save_to_file()
        return f'Your telephone was changed'
    else:
        return f'Sorry, your name {name} doesn\'t exist'

# Виведення телефонного номера по імені
@input_error
def handler_phone(command):
    name = command[0].title()
    if name in TELEPHONEBOOK:
        telephone = TELEPHONEBOOK[name]
        return f'Your contact {name} is {telephone}'
    else:
        return f'Sorry, your name {name} doesn\'t exist'

# Пошук контактів за ім'ям або номером телефону
@input_error
def handler_search(command):
    search_term = command[0].lower()
    matching_contacts = [f'{name}: {phone}' for name, phone in TELEPHONEBOOK.items() if search_term in name.lower() or search_term in phone]
    if matching_contacts:
        return '\n'.join(matching_contacts)
    else:
        return f'No matching contacts found for: {search_term}'

# Виведення всіх контактів
def handler_show_all(*args):
    if TELEPHONEBOOK:
        all_contacts = 'List of contacts\n'
        for name, phone in TELEPHONEBOOK.items():
            all_contacts += f'{name}: {phone}\n'
        return all_contacts
    else:
        return f'Sorry, no contacts in Telephonebook'

# Вивітання
def handler_hello(*args):
    return f'Hello, can I help you?'

# Словник команд і відповідних функцій
COMMANDS = {
    'hello': handler_hello,
    'add': handler_add,
    'change': handler_change,
    'phone': handler_phone,
    'show_all': handler_show_all,
    'search': handler_search
}

# Розбір команд та виклик відповідних функцій
def parser(user_command):
    user_command = user_command.split()
    for key, func in COMMANDS.items():
        if user_command[0].lower() in key:
            return func(user_command[1:])

# Головна функція
def main():
    exit_words = ['good bye', 'bye', 'close', 'thank you', 'exit']
    while True:
        user_input = input('>>> ')
        if user_input in exit_words:
            save_to_file()
            break
        else:
            result = parser(user_input)
            print(result)

if __name__ == '__main__':
    main()
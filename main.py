# Initialize dict here
main_dict = {'name1': 'phone 1',
             'name2': 'phone2'}


# Decorators list here
def decorator_loop(func):
    def wrapper_loop():
        func(*args, **kwargs)
        global values
        values = input('Please enter your command:...')
    return wrapper_loop

def error_handler(func):
    def inner(*args):
        try:
            result = func(*args)
            return result
        except KeyError:
            return "No user with given name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Enter user name"
    return inner
# Function list here

@error_handler
@decorator_loop
def hello():
    print('How can I help you')
    #"hello", отвечает в консоль "How can I help you?"

@error_handler
@decorator_loop
def add(values) -> dict:

    _, new_name, new_phone = str(values.split(' '))
    temp = {new_name:new_phone}
    main_dict.update(temp)
    print(f'New user {new_name} added, his dial number is {new_phone}')
    return main_dict
#"add ...". По этой команде бот сохраняет в памяти (в словаре например) новый контакт.
# Вместо ... пользователь вводит имя и номер телефона, обязательно через пробел.

@error_handler
@decorator_loop
def change(values) -> dict:
    _, old_name, new_phone = str(values.split(' ')) #change User1 000000999995
    main_dict[old_name] = new_phone
    print(f'Existing user {old_name} had changed his phone number to {new_phone}')
    return main_dict
#"change ..." По этой команде бот сохраняет в памяти новый номер телефона для существующего контакта.
# Вместо ... пользователь вводит имя и номер телефона, обязательно через пробел.

@error_handler
@decorator_loop
def phone(values):
    _, old_name = str(values.split(' '))
    phone_number = main_dict.get(old_name)
    print(f'Existing user {old_name} has phone number {phone_number}')

#"phone ...." По этой команде бот выводит в консоль номер телефона для указанного контакта.
# Вместо ... пользователь вводит имя контакта, чей номер нужно показать.

@error_handler
@decorator_loop
def show_all():
    for key, value in main_dict:
        string = '' + key + ':  ' + value + '\n'
        print(string)
    return

#"show all". По этой команде бот выводит все сохраненные контакты с номерами телефонов в консоль.


#MAIN functional
def main():
    print('Bot started')
    while True:
        values = input('Please enter your command:...')
        values = values.lower()
        print()
        match values:
            case "hello":
                hello()
            case "add ...":
                add(values)
            case "change ...":
                change(values)
            case "phone ....":
                phone(values)
            case "show all":
                show_all()
            case "good bye" | "close" | "exit":
                print('Good bye')



if __name__ == '__main__':
    main()

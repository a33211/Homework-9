
main_dict = {'name1': 'phone 1',
             'name2': 'phone2'}

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
def hello(*args):
    return 'How can I help you?'
    #"hello", отвечает в консоль "How can I help you?"

@error_handler
def add(*args) -> str:
    main_dict[args[0]] = args[1]
    return f'New user {args[0]} added, his dial number is {args[1]}'
#"add ...". По этой команде бот сохраняет в памяти (в словаре например) новый контакт.
# Вместо ... пользователь вводит имя и номер телефона, обязательно через пробел.

@error_handler
def change(*args) -> str:
    main_dict[args[0]] = args[1]
    return f'Existing user {args[0]} had changed his phone number to {args[1]}'
#"change ..." По этой команде бот сохраняет в памяти новый номер телефона для существующего контакта.
# Вместо ... пользователь вводит имя и номер телефона, обязательно через пробел.

@error_handler
def phone(*args) -> str:
    print(f'*args {args[0]}')
    return f'Existing user {args[0]} has phone number {main_dict.get(args[0])}'

#"phone ...." По этой команде бот выводит в консоль номер телефона для указанного контакта.
# Вместо ... пользователь вводит имя контакта, чей номер нужно показать.

@error_handler
def show_all(*args):
    result = []
    for k, v in main_dict.items():
        result.append(f"{k} : {v}")
    return "\n".join(result)

#"show all". По этой команде бот выводит все сохраненные контакты с номерами телефонов в консоль.
@error_handler
def exit(*args):
    return "exit"


COMMANDS = {show_all:["show all"],
            hello:["hello"],
            add:["add"],
            change:["change"],
            phone:["phone"],
            exit:["good bye", "close", "exit"]}


def command_parser(user_input:str) -> tuple:
    data = []
    for k, v in COMMANDS.items():
        for item in v:
            if user_input.startswith(item):
                return k, user_input.replace(item, '').strip().split(" ")

#MAIN functional
def main():
    print('Bot started')
    while True:
        values = input('Please enter your command:...')
        command, data = command_parser(values)
        result = command(*data)
        if result == "exit":
            print("Good bye!")
            break
        print(result)



if __name__ == '__main__':
    main()
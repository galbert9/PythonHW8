# Решение команды вундеркиндов
# точка входа программы
# Здесь будет вызываться головной метод из класса DataManager
# Что-то вроде init_system()

#import click

def menu(list_command: dict, invate: str): # принимает на вход словарь
    flag = True
    while flag:
        print(invate)
        command = input('Команда: > ')
        if command in list_command:
            list_command[command]()
            if command != '9':
                click.pause()
        elif command == "0" or not command:
            flag = False
        else:
            print('Этой команды нет')

def main():
    # head_command = {'1': sub_menu_print_base}
    # menu(head_command, menu_head)
    # IO_system.save_data_base('statement', data_manager, '.txt')

    if __name__ == '__main__':
        main()
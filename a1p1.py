# p = 'C:\\Users\\cowvy\\OneDrive\\UCI\\Writing'
# import os
from pathlib import Path

def show_files_then_directories(a_path):
    # a_path = Path(a_path)
    for each_path in a_path.iterdir():
        if each_path.is_file():
            print(each_path)
    for each_path in a_path.iterdir():
        if each_path.is_dir():
            print(each_path)


def show_files_only(a_path):
    # a_path = Path(a_path)
    for each_path in a_path.iterdir():
        if each_path.is_file():
            print(each_path)
    

def show_files_by_extension(a_path, specific_file_type):
    for each_path in a_path.iterdir():
        if each_path.is_file():
            each_path_as_string = str(each_path)
            get_file_extension = each_path_as_string.split('.')
            file_extension = get_file_extension[-1]
            if specific_file_type == file_extension:
                print(each_path)
            

def show_files_by_name(a_path, specific_file_name):
    for each_path in a_path.iterdir():
        if each_path.is_file():
            each_path_as_string = str(each_path)
            get_file_name = each_path_as_string.split('\\')
            file_name = get_file_name[-1]
            if specific_file_name == file_name:
                print(each_path)


def get_given_name(user_input, L_option):
    the_option = user_input.find(L_option)
    given = user_input[(the_option+3):]
    # print(given)
    return given


def program_command():
    while True:
        user_input = input()
        user_input_tokens = user_input.split()

        if user_input_tokens[0] == 'Q':
            break
        elif user_input_tokens[0] == 'L' and len(user_input_tokens) > 1:
            user_path = Path(user_input_tokens[1])
            if len(user_input_tokens) == 2:
                show_files_then_directories(user_path)
                print()
            elif user_input_tokens[2] == '-f':
                show_files_only(user_path)
                print()
            elif user_input_tokens[2] == '-s':
                name = get_given_name(user_input, '-s')
                show_files_by_name(user_path, name)
                print()
            elif user_input_tokens[2] == '-e':
                show_files_by_extension(user_path, user_input_tokens[3])
                print()
        

def main():
    program_command()
    # user_input = 'L C:\\Users\\cowvy\\OneDrive\\UCI\\Writing -f GA final draft guide.pdf'
    # user_input = input()
    # path = user_input.split()
    # show_files_then_directories(path[1])
    # print()
    # show_files_only(path[1])
    # print()
    # show_files_by_name(path[1], "GA final draft guide.pdf")
    # print()
    # show_files_by_extension(path[1], "pdf")


main()

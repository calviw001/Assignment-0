from pathlib import Path


def list_of_paths(a_path):
    paths_list = []
    for each_path in a_path.iterdir():
        paths_list.append(each_path)
    return paths_list


def show_files_then_directories(paths_list):
    for each_path in paths_list:
        if each_path.is_file():
            print(each_path)
    for each_path in paths_list:
        if each_path.is_dir():
            print(each_path)


def show_files_and_directories(paths_list):
    for each_path in paths_list:
            print(each_path)


def show_files_only(paths_list):
    for each_path in paths_list:
        if each_path.is_file():
            print(each_path)
                

def show_files_by_name(paths_list, specific_file_name):
    for each_path in paths_list:
        if each_path.is_file():
            each_path_as_string = str(each_path)
            get_file_name = each_path_as_string.split('\\')
            file_name = get_file_name[-1]
            if specific_file_name == file_name:
                print(each_path)


def show_files_by_extension(paths_list, specific_file_type):
    for each_path in paths_list:
        if each_path.is_file():
            each_path_as_string = str(each_path)
            get_file_extension = each_path_as_string.split('.')
            file_extension = get_file_extension[-1]
            if specific_file_type == file_extension:
                print(each_path)


def recur_list_of_paths(my_path, recur_paths_list):
    for current_path in my_path.iterdir():
        if current_path.is_dir(): #Recursive case
            recur_paths_list.append(current_path)
            recur_list_of_paths(current_path, recur_paths_list)
        else: #Base case
            recur_paths_list.append(current_path)
    return recur_paths_list


def get_given(user_input, L_option):
    the_option = user_input.find(L_option)
    given = user_input[(the_option+3):]
    return given


# class CustomError(Exception):
#     def __init__(self, message="ERROR"):
#         self.message = message

def create_file(path_name, file_name):
    separator_with_pathlib = Path("/").as_posix()
    new_path = str(path_name) + separator_with_pathlib + file_name + '.dsu'
    new_path = Path(new_path)
    new_path.touch()
    if new_path.exists():
        print(new_path)


def delete_file(path_name):
    path_as_string = str(path_name)
    is_dsu = path_as_string.split('.')
    try:
        if is_dsu[-1] == 'dsu':
            path_name.unlink()
            print(path_as_string, 'DELETED')
        else:
            # Not a dsu file
            print("ERROR")
    except FileNotFoundError:
        print("ERROR")


def read_file(path_name):
    path_as_string = str(path_name)
    is_dsu = path_as_string.split('.')
    try:
        if is_dsu[-1] == 'dsu':
            with path_name.open(mode = 'r') as dsu_file:
                content = dsu_file
                if path_name.stat().st_size == 0:
                    print("EMPTY")  
                else:
                    print(content)
        else:
            # Not a dsu file
            print("ERROR")
    except FileNotFoundError:
        print("ERROR")


def check_if_path_exist(path_name):
    return path_name.exists()

def program_command():
    while True:
        user_input = input()
        user_input_tokens = (user_input.strip()).split()
        paths_list = []
        recursive = False

        # PART 1
        if user_input_tokens[0] == 'Q':
            break
        elif user_input_tokens[0] == 'L' and len(user_input_tokens) > 1:
            user_path = Path(user_input_tokens[1])
            if not check_if_path_exist(user_path):
                print("ERROR")
                print()
            elif len(user_input_tokens) >= 3 and user_input_tokens[2] == '-r':
                paths_list = recur_list_of_paths(user_path, paths_list)
                recursive = True
                user_input_tokens.remove('-r')
            else:
                paths_list = list_of_paths(user_path)
            
            if len(user_input_tokens) == 2 and not recursive:
                show_files_then_directories(paths_list)
                print()
            elif len(user_input_tokens) == 2 and recursive:
                show_files_and_directories(paths_list)
                print()
            elif user_input_tokens[2] == '-f':
                show_files_only(paths_list)
                print()
            elif user_input_tokens[2] == '-s':
                name = get_given(user_input, '-s')
                show_files_by_name(paths_list, name)
                print()
            elif user_input_tokens[2] == '-e':
                extension = get_given(user_input, '-e')
                show_files_by_extension(paths_list, extension)
                print()
        
        # PART 2
        else:
            user_path = Path(user_input_tokens[1])
            if not check_if_path_exist(user_path):
                print("ERROR")
                print()
            elif user_input_tokens[0] == 'C' and len(user_input_tokens) > 1:
                file_name = user_input_tokens[3]
                create_file(user_path, file_name)
                print()
            elif user_input_tokens[0] == 'D' and len(user_input_tokens) == 2:
                delete_file(user_path)
                print()
            elif user_input_tokens[0] == 'R' and len(user_input_tokens) == 2:
                read_file(user_path)
                print()
   

def main():
    program_command()
   

main()

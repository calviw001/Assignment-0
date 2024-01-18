# p = 'C:\\Users\\cowvy\\OneDrive\\UCI\\Writing'
import os


def show_files_then_directories(a_path):
    directory_contents = os.listdir(a_path)
    for content in directory_contents:
        each_path = a_path + os.path.sep + content
        if os.path.isfile(each_path):
            print(each_path)
    for content in directory_contents:
        each_path = a_path + os.path.sep + content
        if not os.path.isfile(each_path):
            print(each_path)


def show_files_only(a_path):
    directory_contents = os.listdir(a_path)
    for content in directory_contents:
        each_path = a_path + os.path.sep + content
        if os.path.isfile(each_path):
            # print(content)
            print(each_path)


def show_files_by_extension(a_path, file_type):
    directory_contents = os.listdir(a_path)
    for content in directory_contents:
        each_path = a_path + os.path.sep + content
        if os.path.isfile(each_path):
            if file_type in content:
                print(each_path)


def show_files_by_name(a_path, file_name):
    directory_contents = os.listdir(a_path)
    for content in directory_contents:
        each_path = a_path + os.path.sep + content
        if os.path.isfile(each_path):
            if file_name == content:
                print(each_path)


def get_given(user_input, L_option):
    the_option = user_input.find(L_option)
    given = user_input[(the_option+3):]
    print(given)
    return given


def program_command():
    while True:
        user_input = input()
        user_path = user_input.split()

        if user_path[0] == 'Q':
            break
        elif user_path[0] == 'L' and len(user_path) > 1:
            if len(user_path) == 2:
                show_files_then_directories(user_path[1])
                print()
            elif user_path[2] == '-f':
                show_files_only(user_path[1])
                print()
            elif user_path[2] == '-s':
                name = get_given(user_input, '-s')
                show_files_by_name(user_path[1], name)
                print()
            elif user_path[2] == '-e':
                show_files_by_extension(user_path[1], user_path[3])
                print()
        

def main():
    program_command()
    # user_input = 'L C:\\Users\\cowvy\\OneDrive\\UCI\\Writing -s GA final draft guide.pdf'
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

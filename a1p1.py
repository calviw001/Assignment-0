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


def program_command():
    pass


def main():
    user_input = 'Q C:\\Users\\cowvy\\OneDrive\\UCI\\Writing'
    # user_input = input()
    path = user_input.split()
    # show_files_then_directories(path[1])
    # print()
    show_files_only(path[1])
    # print()
    # show_files_by_name(path[1], "GA final draft guide.pdf")
    # print()
    # show_files_by_extension(path[1], "pdf")

main()

def space(num):
    i = 0
    a_space = ''
    while i < num:
        a_space += '  '
        i += 1
    return a_space


def main():
    num_rectangles = int(input())
    count = 0
    while count < num_rectangles:
        print("+-+")
        print(f"{space(count)}" + "| |")
        print(f"{space(count)}" + "+-", end='')
    #     print(f"{rect()} + {tab(count)}", end='')
    #     # if count == 0:
    #     #     diagonal_rect = rectangle()
    #     #     print(diagonal_rect)
    #     # else:
    #     #     diagonal_rect += rectangle()
    #     #     print(diagonal_rect)
        count +=1
    print("+\n")


main()

if __name__ == '__main__':
    n = int(input())
    my_list = []

    for _ in range(n):
        command = input().split()
        operation = command[0]

        if operation == "insert":
            i = int(command[1])
            e = int(command[2])
            my_list.insert(i, e)
        elif operation == "print":
            print(my_list)
        elif operation == "remove":
            e = int(command[1])
            my_list.remove(e)
        elif operation == "append":
            e = int(command[1])
            my_list.append(e)
        elif operation == "sort":
            my_list.sort()
        elif operation == "pop":
            my_list.pop()
        elif operation == "reverse":
            my_list.reverse()
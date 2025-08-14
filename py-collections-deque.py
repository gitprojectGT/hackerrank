from collections import deque

main_deque = deque()
if __name__ == '__main__':
    n = int(input())
    if n < 0:
        print("Negative")
    elif n == 0:
        print("Zero")
        exit(0)

    for _ in range(n):
        command = input().split()
        if command[0] == 'append':
            main_deque.append(int(command[1]))
        elif command[0] == 'appendleft':
            main_deque.appendleft(int(command[1]))
        elif command[0] == 'pop':
            main_deque.pop()
        elif command[0] == 'popleft':
            main_deque.popleft()

    print(*main_deque)
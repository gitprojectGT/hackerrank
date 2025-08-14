if __name__ == '__main__':
    s = set()
    n = int(input())
    for i in range(n):
        x = int(input())
        if x not in s and x.isdigit() and int(x) >= 0:
            s.add(x)
        print(s)

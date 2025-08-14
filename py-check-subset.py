if __name__ == '__main__':
    T= int(input())
    for i in range(T):
        n = int(input())
        set_a = set(map(int, input().split()))
        m = int(input())
        set_b = set(map(int, input().split()))
        if set_a.issubset(set_b):
            print(True)
        else:
            print(False)
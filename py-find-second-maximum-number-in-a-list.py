if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    print(sorted(s)[-2])  # Sort the set and print the second last element
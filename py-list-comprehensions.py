if __name__ == '__main__':
    x   = int(input())
    y   = int(input())
    z   = int(input())
    n   = int(input())
    # it is x+1 because we want to include the value x in the range
    # it is y+1 because we want to include the value y in the range
    # it is z+1 because we want to include the value z in the range
    # it is (i + j + k) != n because we want to exclude the
    # combinations where the sum of i, j, and k equals n
    # the result is a list of lists where each inner list contains
    # the values of i, j, and k
    result = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n]
    print(result)
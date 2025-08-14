def can(cubes):
    left = 0
    right = len(cubes) - 1
    last_placed_cube = max(cubes) + 1

    while left <= right:
        if cubes[left] >= cubes[right]:
            current_cube = cubes[left]
            left += 1
        else:
            current_cube = cubes[right]
            right -= 1
        if current_cube > last_placed_cube:
            return "No"

        last_placed_cube = current_cube
    return "Yes"


if __name__ == '__main__':

    t = int(input())
    for _ in range(t):
        n = int(input())
        cubes = list(map(int, input().split()))
        print(can(cubes))

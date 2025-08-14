
if __name__ == '__main__':
    n_student = int(input())
    set_student = set(map(int, input().split()))
    n_french_student = int(input())
    set_french_student = set(map(int, input().split()))
    print(len(set_student.symmetric_difference(set_french_student)))
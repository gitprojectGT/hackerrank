if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_scores = sum(student_marks[query_name])/ len(student_marks[query_name])
    print(f"{query_scores:.2f}")
# The code calculates the average score of a student based on their name.
# It first reads the number of students and their scores, storing them in a dictionary.
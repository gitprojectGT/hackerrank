if __name__ == '__main__':
    scores = []
    nested = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        nested.append([score, name])

    unique_score = sorted(set(scores))
    print(unique_score)
    second_score = unique_score[1]
    print(second_score)
    names = [name for score, name in nested if score == second_score]

    for name in sorted(names):
        print(name)
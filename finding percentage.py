if __name__ == '__main__':
    n = int(input())
    avg = 0
    sum1 = 0
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for v in student_marks[query_name]:
        sum1 = sum1 + v
        avg = (sum/3)
    print("%.2f" % avg)
    
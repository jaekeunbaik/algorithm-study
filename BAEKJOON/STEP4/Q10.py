N = int(input())
grades = list(map(int, input().split()))

max_grade = max(grades)

for i in range(N):
    grades[i] = grades[i] / max_grade * 100

print(sum(grades) / N)

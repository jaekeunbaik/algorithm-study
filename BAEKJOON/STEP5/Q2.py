piece = list(map(int, input().split()))
standard = [1, 1, 2, 2, 2, 8]
result = [s - p for s, p in zip(standard, piece)]
print(*result)
S = input()
print(len(S))

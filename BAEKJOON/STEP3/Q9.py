import sys

input = sys.stdin.readline

T = int(input())
results = []

for i in range(1, T + 1):
    results.append("*" * i)

sys.stdout.write('\n'.join(map(str, results)))
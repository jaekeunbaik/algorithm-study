numbers = [int(input()) for _ in range(10)]
remainders = set()

for num in numbers:
    remainders.add(num % 42)

print(len(remainders))
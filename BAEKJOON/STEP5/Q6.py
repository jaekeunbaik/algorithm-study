S = input()

for ch in range(ord('a'), ord('z') + 1):
    print(S.find(chr(ch)), end=' ')
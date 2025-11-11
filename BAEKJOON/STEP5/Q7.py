for _ in range(int(input())):
    R, S = input().split()
    print(''.join(ch * int(R) for ch in S))
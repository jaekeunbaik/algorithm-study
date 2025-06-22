def find_max_occurred_alphabet(string):
    arr = [0] * 26
    for char in string:
        if not char.isalpha():
            continue
        num = ord(char)-ord('a')
        arr[num] = arr[num] + 1
    max_index = max(arr) + ord('a')
    print(max_index)
    return 1


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))
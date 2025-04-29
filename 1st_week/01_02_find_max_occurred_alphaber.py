def find_max_occurred_alphabet(string):
    alphabet_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    max_occurrence = 0
    max_alphabet = alphabet_array[0]

    for alphabet in alphabet_array:
        occurence = 0
        for char in string:
            if char == alphabet:
                occurence += 1
        if occurence > max_occurrence:
            max_alphabet = alphabet
            max_occurrence = occurence
    return max_alphabet
 
result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))


def find_max_occurred_alphabet2(string):
    alphabet_occurrence_array = [0] * 26
    for char in string:
        if char.isalpha():
            alphabet_occurrence_array[ord(char) - ord('a')] += 1    
    max_occrurrence = 0
    max_alphabet_index = 0

    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence > max_occrurrence:
            max_occrurrence = alphabet_occurrence
            max_alphabet_index = index
    return chr(max_alphabet_index + ord('a'))
    



result = find_max_occurred_alphabet2
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))
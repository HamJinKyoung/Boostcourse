""" 세자리 수를 곱해 만들 수 있는 가장 큰 대칭수

앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수(palindrome)라고 부릅니다.

두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (= 91 × 99) 입니다.

세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 얼마입니까? """

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def find_max_palindrome():
    max = 0
    for n1 in range(999, 99, -1):
        for n2 in range(999, 99, -1):
            n3 = n1 * n2
            if is_palindrome(n3) and n3 > max:
                max = n3
    return max
 
print(find_max_palindrome())
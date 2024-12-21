from itertools import count

input = 10


def find_prime_list_under_number(number):

    # 소수는 1과 자기 자신을 제외한 다른 수를 곱하여 만들 수 없는 숫자이다.
    # 문제는 어떤 숫자릅 입력했을 때 자기 자신보다는 작되, 소수인 숫자를 리스트로 반환한다.
    # input = 5 -> output = 2,3 (1은 소수가 아님, 예외 처리를 해야함, 0 보다 큰 예외 처리도 필요)
    list_under_number = []

    for i in range(2, number + 1):
        for j in list_under_number:
            if i % j == 0 and j * j <= i:
                break
        else:
            list_under_number.append(i)
    return list_under_number


result = find_prime_list_under_number(input)
print(result)
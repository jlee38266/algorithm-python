# input_string = "011110"
input_string = "11001100110011000001"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 일단 결과에는 count가 필요할 것 같음
    # 문자열로 데이터가 들어왔을 때, 0 또는 1로 전부 변환을 해줘야 하는상황
    # 연속된 구간의 수를 세는 것이 필요함
    count_to_all_zero = 0
    count_to_all_one = 0

    if string[0] == "1":
        count_to_all_zero += 1
    else:
        count_to_all_one += 1

    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            if string[i+1] == "0":
                count_to_all_zero += 1
            else:
                count_to_all_one += 1
    return min(count_to_all_zero, count_to_all_one)

result = find_count_to_turn_out_to_all_zero_or_all_one(input_string)
print(result)
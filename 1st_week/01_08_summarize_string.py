
def summarize_string(input_str):

    count = 0
    result_str = ''

    for i in range(len(input_str)-1):
        if input_str[i] == input_str[i+1]:
            count += 1
        else:
            result_str += input_str[i] + str(count + 1) + '/'
            count = 0

    result_str += input_str[len(input_str)-1] + str(count + 1)

    return result_str


input_str = "acccdeeeffffffffgggggg"
result = summarize_string(input_str)
print(result)


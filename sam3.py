def numbers(input_string):
    digit_count = {}
    for digit in input_string:
        digit = int(digit)
        digit_count[digit] = digit_count.get(digit, 0) + 1
    sorted_digit_count = sorted(digit_count.items(), key=lambda x: x[1], reverse=True)
    top_three = sorted_digit_count[:3]
    result_dict = {digit: count for digit, count in top_three}
    return result_dict
print(numbers(input()))
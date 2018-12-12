'''

https://www.geeksforgeeks.org/find-next-greater-number-set-digits/

Input:  n = "218765"
Output: "251678"

Input:  n = "1234"
Output: "1243"

Input: n = "4321"
Output: "Not Possible"

Input: n = "534976"
Output: "536479"

'''


def get_next_permutation(input_num):
    input_list = map(int, input_num)[::-1]
    if all(input_list[i] <= input_list[i + 1] for i in xrange(len(input_list) - 1)):
        return 'Not Possible'
    for idx in xrange(len(input_list)):
        if idx > 0:
            if input_list[idx] < input_list[idx - 1]:
                break
    input_list[idx], input_list[0] = input_list[0], input_list[idx]
    return ''.join(str(i) for i in input_list[idx:][::-1] + input_list[:idx])


if __name__ == '__main__':
    assert get_next_permutation("1234") == '1243'
    assert get_next_permutation('4321')== 'Not Possible'
    assert get_next_permutation('218765')== '251678'
    assert get_next_permutation('534976')== '536479'
    assert get_next_permutation('2987')== '7289'

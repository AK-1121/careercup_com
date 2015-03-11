# http://www.careercup.com/question?id=5684278553739264


def max_length(string):
    # Error code in case of empty string:
    str_len = len(string)
    if str_len == 0:
        return -1

    max_len = 1
    # Take each letter from the first to the last in the string and find
    # find substring with unique letters:
    for i in range(0, str_len):
        tmp = string[i]
        flag = True
        j = i + 1
        while flag and (j < str_len):
            if string[j] not in tmp:
                tmp += string[j]
            else:
                flag = False
            j += 1

        if len(tmp) > max_len:
            max_len = len(tmp)

        # We won`t be able to find longer string if statement is True, so
        # terminate for-loop and return max_len:
        if max_len >= str_len - i:
            return max_len

    return max_len


if __name__ == '__main__':
    str = input("Give me string: ")
    print(max_length(str))

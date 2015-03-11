# http://www.careercup.com/question?id=15555796
from collections import Counter
compare = lambda x, y: Counter(x) == Counter(y)
# collections.Counter - multiset: http://en.wikipedia.org/wiki/Multiset

def a_is_anagram_in_b(a, b):
    len_a = len(a)
    a_list = list(a)
    flag = False
    for i in range(0, len(b)-len(a)+1):
        if compare(a_list, list(b[i:i+len_a])):
            flag = True
    return flag

if __name__ == '__main__':
    a = input("Give me smalll string:")
    b = input("Give me big string:")
    print("The result is", str(a_is_anagram_in_b(a,b)))

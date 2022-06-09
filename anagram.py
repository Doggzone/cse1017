# Anagram(어구전철(語句轉綴))
# Dynamic programming 문제

def sort_string(digits):
    # sort a string in an ascending order
    # in: digits, a string
    # out: key, a sorted string
    # convert a string into a list of characters
    digits = list(digits)
    # sort the list
    digits.sort()
    # convert the sorted list back to string
    key = ''
    return key.join(digits)

def find_anagrams(d4s):
    # find all anagrams in the list of 4-digit strings
    # in: d4s, list of 4-digit strings
    # out: print anagrams

    # group strings according to the key (= sorted string)    
    candidates = {}
    for d4 in d4s:
        key = sort_string(d4)
        if key in candidates:
            anagram = candidates[key]
            anagram.add(d4)
            candidates[key] = anagram
        else:
            candidates[key] = {d4}
    # collect anagrams from candidate group
    anagrams = {}
    for key in candidates:
        if len(candidates[key]) > 1:
            anagrams[key] = candidates[key]
    # print anagrams
    for key in anagrams:
        for d4 in anagrams[key]:
            print(d4,end=' ')
        print()

d1 = ['0952', '5239', '1270', '8581', '7458', '3414', '7906', '2356', '4360', '3491', '6232', '5927', '2735', '2509', '5849', '8457', '9340', '1858', '8602', '5784']
# find_anagrams(d1)
# 2509 0952 
# 8581 1858 
# 7458 8457 5784  

d2 = ['1112','1112','1211','2111','1211','1121','1112']
# find_anagrams(d2) 
# 1112 1211 1121 2111

d3 = ['1111','1111','1111','1111']
# find_anagrams(d3) 
# prints nothing

d4 = ['0000','7890']
# find_anagrams(d4)
# prints nothing

d5 = []
# find_anagrams(d5)
# prints nothing

# function for random test-case generation
def random_4_digits(k):
    # create a list of k random 4-digit strings
    # in: k, the number of strings to create
    # out: sample_strings, list of k random 4-digit strings 
    import random
    all_numbers = set(range(10000)) # create a set of 0 ~ 9999
    sample_numbers = random.sample(all_numbers,k) # randomly sample k numbers
    sample_strings = []
    for n in sample_numbers:
        if 1000 <= n <= 9999:
            sample_strings.append(str(n))
        elif 100 <= n <= 999:
            sample_strings.append('0' + str(n))
        elif 10 <= n <= 99:
            sample_strings.append('00' + str(n))
        else:
            sample_strings.append('000' + str(n))
    return sample_strings
print(find_anagrams(random_4_digits(100)))

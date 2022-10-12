from math import factorial
from string import ascii_uppercase


def dec_2_fact_string(nb):
    result, i = "", 1
    while nb:
        number = str(nb % i)
        if int(number) > 9:
            number = ascii_uppercase[int(number) - 10]
        result += number
        nb //= i
        i += 1
    return result[::-1]


def fact_string_2_dec(string):
    result = 0
    for i in range(len(str(string))):
        number = string[-(i + 1)]
        if number in ascii_uppercase:
            number = ascii_uppercase.index(number) + 10
        result += factorial(i) * int(number)
    return result


print(dec_2_fact_string(463))

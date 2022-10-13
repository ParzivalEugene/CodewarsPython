class RomanNumerals:
    def to_roman(arabic_value: int):
        data = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'),
        ]
        res = ""
        for arabic_int, roman_int in data:
            quotient, arabic_value = arabic_value // arabic_int, arabic_value % arabic_int
            res += roman_int * quotient
        return res

    def from_roman(roman_value: str):
        data = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'),
        ]
        res, position = 0, 0
        length = len(roman_value)
        while position < length:
            if position + 1 < length and roman_value[position: position + 2] in [_[1] for _ in data]:
                res += [_[0] for _ in data if roman_value[position: position + 2] == _[1]][0]
                position += 2
            else:
                res += [_[0] for _ in data if roman_value[position] == _[1]][0]
                position += 1
        return res

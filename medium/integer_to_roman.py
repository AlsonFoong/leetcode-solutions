# Time: O(1) - Loop execution and all operations run in constant time
# Space: O(1) - Variables either take up fixed memory or never exceed constraints
class Solution:
    def intToRoman(self, num: int) -> str:
        value_symbols = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
            (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

        output = []

        for value, symbol in value_symbols:
            if num == 0:
                break
            count = num // value
            output.append(symbol * count)
            num -= value * count
        
        return ''.join(output)

class RomanNumeralConverter:
    def __init__(self):
        self.roman_numerals = {
            'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5,
            'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10,
            'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

    def roman_to_integer(self, roman_numeral):
        total = 0
        prev_value = 0
        for numeral in reversed(roman_numeral):
            value = self.roman_numerals[numeral]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total


converter = RomanNumeralConverter()
print(converter.roman_to_integer("MMCML"))

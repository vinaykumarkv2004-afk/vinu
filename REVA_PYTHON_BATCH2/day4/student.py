def int_to_Roman(self, num):
        integer_vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_equal = ["M", "CM", "D", "CD", "C", "XC",
                       "L", "XL", "X", "IX", "V", "IV", "I"]

        roman_str = ""

        for i in range(len(integer_vals)):
            while num >= integer_vals[i]:
                roman_str += roman_equal[i]
                num -= integer_vals[i]

        return roman_str


# Main Program
n = int(input())
obj = intToRomanConvertor()
print(obj.int_to_Roman(n))


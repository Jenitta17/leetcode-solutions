class Solution(object):
    def multiply(self, num1, num2):
        digits = "0123456789"
        def to_number(s):
            value = 0
            for ch in s:
                value = value * 10 + digits.index(ch)
            return value
        a = to_number(num1)
        b = to_number(num2)
        product = a * b
        if product == 0:
            return "0"
        result = ""
        while product > 0:
            result = digits[product % 10] + result
            product = product // 10
        return result

class Solution(object):
    def addBinary(self, a, b):
        while len(a) < len(b):
            a = "0" + a
        while len(b) < len(a):
            b = "0" + b
        carry = 0
        result = ""
        for i in range(len(a) - 1, -1, -1):
            total = carry
            if a[i] == "1":
                total = total + 1
            if b[i] == "1":
                total = total + 1
            if total == 0:
                result = "0" + result
                carry = 0
            elif total == 1:
                result = "1" + result
                carry = 0
            elif total == 2:
                result = "0" + result
                carry = 1
            else:
                result = "1" + result
                carry = 1
        if carry == 1:
            result = "1" + result

        return result

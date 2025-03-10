class Solution(object):
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]
    
sol = Solution()
print(sol.addBinary('11', '1'))

class Solution(object):
    def addBinary(self, a, b):
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []

        while i > 0 or j > 0 or carry:
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >=0  else 0

            total = digit_a + digit_b + carry
            carry = total // 2 # Если 2 или 3, перенос = 1, иначе 0
            result.append(str(total % 2))

            i -= 1
            j -= 1

        return ''.join(result[::-1])
 
sol = Solution()
print(sol.addBinary('11', '1'))
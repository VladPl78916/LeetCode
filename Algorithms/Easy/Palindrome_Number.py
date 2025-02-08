class Solution(object):
    def isPalindrome(self, x):
        if str(x) == str(x)[::-1]:
            return True
        return False

# Оптимизированное решение за O(log(n)) и без дополнительной памяти

class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        return reversed_half == x or x == reversed_half // 10
    
sol = Solution()
print(sol.isPalindrome(121))
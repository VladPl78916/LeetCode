class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)

# Оптимизированное решение за O(n), ещё бы и догадаться, что это числа Фибоначчи

class Solution(object):
    def climbStairs(self, n):
        if n <= 1:
            return 1
        
        dp = [0] * (n + 1)

        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
    
# Оптимизация по памяти

class Solution(object):
    def climbStairs(self, n):
        if n <= 1:
            return 1
        
        prev1 = 1
        prev2 = 1

        for i in range(2, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current

        return prev1
    
sol = Solution()
print(sol.climbStairs(38))   
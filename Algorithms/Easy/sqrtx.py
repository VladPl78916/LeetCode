class Solution(object):
    def mySqrt(self, x):
        if x < 2:
            return x
        if x < 0:
            return
        
        left, right = 2, x // 2
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == x:
                return mid
            
            elif square < x:
                left = mid + 1

            else:
                right = mid - 1

        return right
    
sol = Solution()
print(sol.mySqrt(8))
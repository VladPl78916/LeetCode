class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k, nums
    
sol  = Solution()
print(sol.removeElement([3,2,2,3], 3))

# Без указателей
class Solution(object):
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)

sol  = Solution()
print(sol.removeElement([3,2,2,3], 3))
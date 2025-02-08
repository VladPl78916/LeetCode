nums = list(map(int, input("Введите числа через пробел: ").split()))
target = int(input("Введите таргет: "))
output = []

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            output.append(i)
            output.append(j)
            break
print(output)

# Оптимизированное решение за O(n)

class Solution(object):
    def twoSum(self, nums, target):
        num_dict = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_dict:
                return [num_dict[complement], i]
            
            num_dict[num] = i
        return []
    
sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))  # Вывод: [0, 1]
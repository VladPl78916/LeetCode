class Solution(object):
    def lengthOfLastWord(self, s):
        return len(s.strip().split()[-1])
    
sol = Solution()
print(sol.lengthOfLastWord('   fly me   to   the moon  '))
class Solution(object):
    def longestCommonPrefix(self, strs):

        if not strs:
            return ""
        
        min_length = min(len(s) for s in strs)
        s_output = ''

        for k in range(min_length):
            char = strs[0][k]
            for i in range(1, len(strs)):
                if strs[i][k] != char:
                    return s_output
            s_output += char

        return s_output
    
# Решение за O(N log N + M)
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        strs.sort() 
        first, last = strs[0], strs[-1]  
        min_length = min(len(first), len(last))

        for i in range(min_length):
            if first[i] != last[i]:
                return first[:i]
        return first[:min_length]

sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))
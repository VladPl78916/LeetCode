class Solution(object):
    def strStr(self, haystack, needle):
        
        if not needle:
            return 0

        p = [0] * len(needle)
        j = 0 
        i = 1 

        while i < len(needle):
            if needle[i] == needle[j]:
                p[i] = j + 1
                i += 1
                j += 1
            else:
                if j > 0:
                    j = p[j - 1]
                else:
                    p[i] = 0
                    i += 1

        m = len(needle)
        n = len(haystack)

        i = 0  
        j = 0 
        
        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == m:
                    return i - m  
            else:
                if j > 0:
                    j = p[j - 1]
                else:
                    i += 1

        return -1

sol = Solution()
print(sol.strStr('sadbutsad', 'sad'))

# Второй способ

class Solution(object):
    def strStr(self, haystack, needle):
        x = ""
        if needle not in haystack:
            return -1
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                x = haystack[i:i + len(needle)]
                if needle == x:
                    return i
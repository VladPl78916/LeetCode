class Solution(object):
    def romanToInt(self, s):
        dict_roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        sum_int = 0

        for i in range(len(s) - 1):
            if dict_roman[s[i]] < dict_roman[s[i + 1]]:
                sum_int -= dict_roman[s[i]]
            else:
                sum_int += dict_roman[s[i]]
                
        sum_int += dict_roman[s[-1]]
        return sum_int

sol = Solution()
print(sol.romanToInt('MCMXCIV'))
class Solution(object):
    def isValid(self, s):
        stack = []
        flag = True

        for lt in s:

            if lt in '([{':
                stack.append(lt)

            elif lt in ')]}':
                if len(stack) == 0:
                    flag = False
                    break
                
                br = stack.pop()
                if br == '(' and lt == ')':
                    continue
                if br == '[' and lt == ']':
                    continue
                if br == '{' and lt == '}':
                    continue
                
                flag = False
                break
        if len(stack) == 0 and flag:
            return True
        else:
            return False
        
# Более оптимизированный вариант
class Solution:
    def isValid(self, s):
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in pairs:
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                stack.append(char)
        
        return not stack

sol = Solution()
print(sol.isValid('([])'))
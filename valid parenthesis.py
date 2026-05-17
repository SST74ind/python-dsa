class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        L=[]
        brac={')':'(', ']':'[', '}':'{'}
        for i in s:
            if i in brac:
                if L and L[-1]==brac[i]:
                    L.pop()
                else:
                    return False
            else:
                L.append(i)
        return not L
# Example usage:
solution = Solution()
print(solution.isValid("()"))  # Output: True
print(solution.isValid("()[]{}"))  # Output: True
print(solution.isValid("(]"))  # Output: False
print(solution.isValid("([)]"))  # Output: False
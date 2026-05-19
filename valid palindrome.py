#APPROACH 1: String cleaning+reverse-O(n)
#Fragile, manual punctuation list can miss characters
class Solution1(object):
    def isPalindrome(self, s):
        p="!@#$%^&*\(){}[]_-:;,`.?'/\""
        s=s.replace(" ", "")
        s=s.lower()
        for i in p:
            s=s.replace(i, "")
        return s==s[::-1]
#Example usage:
solution=Solution1()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # True
print(solution.isPalindrome("race a car"))  # False

#APPROACH 2: Two Pointers+isalnum()-O(n)
#Optimal, handles ALL special characters
#automatically, O(1) space
class Solution2(object):
    def isPalindrome(self, s):
        l,r = 0,len(s)-1
        while l<r:
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r-=1
            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
        return True
#Example usage:
solution=Solution2()
print(solution.isPalindrome("No 'x' in Nixon"))  # True
print(solution.isPalindrome("Hello, World!"))  # False
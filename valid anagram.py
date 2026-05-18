# APPROACH 1: Count frequency-O(26n) time
# My original solution-fastest on small inputs
class Solution1(object):
    def isAnagram(self, s, t):
        x='abcdefghijklmnopqrstuvwxyz'
        for i in x:
            if s.count(i)!=t.count(i):
                return False
        return True
#Example usage:
solution=Solution1()
print(solution.isAnagram("listen", "silent"))  # True
print(solution.isAnagram("hello", "bello"))    # False

# APPROACH 2: Counter-O(n) time
# Cleanest code, slower on small inputs due to dictionary creation overhead
from collections import Counter
class Solution2(object):
    def isAnagram(self, s, t):
        return Counter(s)==Counter(t)
#Example usage:
solution=Solution2()
print(solution.isAnagram("anagram", "nagaram"))  # True
print(solution.isAnagram("rat", "car"))          # False

# APPROACH 3: HashMap-O(n) time
class Solution3(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        count={}
        for c in s:
            count[c]=count.get(c, 0)+1
        for c in t:
            count[c]=count.get(c, 0)-1
            if count[c]<0:
                return False
        return True
#Example usage:
solution=Solution3()
print(solution.isAnagram("limes", "slime"))  # True
print(solution.isAnagram("great", "grate"))  # True
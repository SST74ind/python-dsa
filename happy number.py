class Solution(object):
    def isHappy(self, n):
        def get_next(n):
            s=0
            while n>0:
                d=n%10
                s+=d*d
                n//=10
            return s
        slow=n
        fast=get_next(n)
        while slow!=1 and slow!=fast:
            slow=get_next(slow)
            fast=get_next(get_next(fast))
        return fast==1
# Example usage:
solution = Solution()
print(solution.isHappy(19))
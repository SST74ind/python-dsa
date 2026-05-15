class Solution(object):
    def isHappy(self, n):
        def get_next(n):
            s=0
            while n>0:
                d=n%10
                s+=d*d
                n//=10
            return s
        tortoise=n
        hare=get_next(n)
        while hare!=1 and tortoise!=hare:
            tortoise=get_next(tortoise)
            hare=get_next(get_next(hare))
        return hare==1
# Example usage:
solution = Solution()
print(solution.isHappy(19))
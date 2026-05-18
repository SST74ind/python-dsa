#time complexity: O(n)
#space complexity: O(1)
class Solution(object):
    def maxProfit(self, prices):
        minp=float('inf')
        prof=0
        for i in prices:
            if i<minp:
                minp=i
            elif i-minp>prof:
                prof=i-minp
        return prof
# Example usage:
solution=Solution()
print(solution.maxProfit([7,1,5,3,6,4]))  # Output: 5
print(solution.maxProfit([1,2,3,4,5]))  # Output: 4
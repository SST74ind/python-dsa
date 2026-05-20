#space complexity: O(1)
#time complexity: O(n)
class Solution(object):
    def minCostClimbingStairs(self, cost):
        cost.append(0)
        for i in range(len(cost)-3,-1,-1):
            cost[i]=cost[i]+min(cost[i+1],cost[i+2])
        return min(cost[i],cost[i+1])
#Example usage:
solution=Solution()
print(solution.minCostClimbingStairs([10, 15, 20]))  # Output: 15
print(solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # Output: 6
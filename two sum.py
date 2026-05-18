#APPROACH 1: Brute Force-O(n²) time, O(1) space
#Check every pair of numbers
class SolutionBruteForce(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]

#APPROACH 2: HashMap-O(n) time, O(n) space
#Store each number and check if complement exists
#This is 100x faster on large inputs
class SolutionOptimal(object):
    def twoSum(self, nums, target):
        seen={}
        for i, num in enumerate(nums):
            complement=target-num
            if complement in seen:
                return [seen[complement], i]
            seen[num]=i
nums=[2, 7, 11, 15]
target=9
print("Brute Force:",SolutionBruteForce().twoSum(nums, target))
print("Optimal:    ",SolutionOptimal().twoSum(nums, target))
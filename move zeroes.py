#space complexity: O(1)
#time complexity: O(n)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[l]=nums[i]
                l+=1
        while l<len(nums):
            nums[l]=0
            l+=1
#Example usage:
solution=Solution()
nums=[0,1,0,3,12]
solution.moveZeroes(nums)
print(nums)
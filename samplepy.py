class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        if nums:
            for j in range(1,len(nums)):
                if nums[j] != nums[i]:
                    i+=1
                    nums[i] = nums[j]
            return i+1
        else:
            return 0
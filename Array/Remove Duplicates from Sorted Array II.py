from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numsLen = len(nums)
        if  numsLen <= 2:
            return numsLen
        i=2
        for j in range(2,numsLen):
            if nums[i-2] != nums[j]:
                nums[i] = nums[j]
                i=i+1
        return i
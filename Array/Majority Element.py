from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        counter = 1
        print(nums)
        value = nums[0]
        for i in range(1,len(nums)+1):
            if counter>len(nums)/2:
                return value
            if i == len(nums):
                return None
            if nums[i]!=nums[i-1]:
                counter = 1
                value = nums[i]
                print(value)
            else:
                counter = counter+1
                print(f'counter {counter} value: {value}')

instance = Solution()

print(instance.majorityElement([3,2,3]))
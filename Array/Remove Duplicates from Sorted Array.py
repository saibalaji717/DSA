# Importing the List type from typing
from typing import List
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         p1,p2=0,0
#         while p2<len(nums):
            
#             if nums[p1]==nums[p2]:
#                 pass
#             else:
#                 print(f'P1 {nums[p1]} P2 {nums[p2]}')
#                 nums[p1+1] = nums[p2]
#                 p1=p1+1
#             p2=p2+1
#         print(nums)
#         return p1+1
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      p1=1
      for p2 in range(1,len(nums)):
         if(nums[p2]!=nums[p2-1]):
            nums[p1]=nums[p2]
            p1=p1+1
      return p1
instance = Solution()

print(instance.removeDuplicates([1,1,2]))

# 0 - no 
# 1-replace
# 
# 
# 

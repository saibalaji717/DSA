# Importing the List type from typing
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize two pointers, p1 and p2, both set to the beginning of the list.
        p1, p2 = 0, 0

        # Iterate through the list using pointer p2.
        while p2 < len(nums):
            # Check if the element at position p2 is not equal to the specified value (val).
            if nums[p2] != val:
                # If not equal, update the element at position p1 to be the element at position p2.
                nums[p1] = nums[p2]
                # Increment p1 to point to the next position where a non-val element should be placed.
                p1 += 1

            # Increment p2 to move to the next element in the list.
            p2 += 1

        # Return the value of p1, representing the length of the modified list.
        return p1


# Given input
nums = [3, 2, 2, 3]
val = 3

# Calling the removeElement method
length = Solution.removeElement( {},nums, val)
print(length)
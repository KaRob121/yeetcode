"""
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 
Constraints:
> 1 <= nums.length <= 1000
> -231 <= nums[i] <= 231 - 1
> nums[i] != nums[i + 1] for all valid i.

Follow up: Could you implement a solution with logarithmic complexity?
"""

# THOUGHTS
# This problem was not too bad for a medium problem!
# However, after reading the solution, I realized that problem could be solved with O(log n) time and space complexity using binary search.
# After reading the follow up note in the problem description, I was confused since I assumed a logarithmic complexity implied sorting, and that doesn't make sense in this scenario. 
# I didn't realize that it can also imply searching.
# It's cool that we can use binary search for this problem even without sorting the array!
# I also didn't realize that if the current number being looked at is greater than its right neighbor, then it will a peak element. Thus, I could have cut the number of lines of code it takes to solve this problem down from what I have in attempt 1. 

# ------------- ATTEMPT 1

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
    """
    Finds a peak element (an element who is greater than its left and right neighbor) in a list and returns its index.

    This runs in O(n) time, where n is the length of the passed array and has O(1) space complexity.
    """
        nums_length = len(nums)
        if nums_length == 1:
            return 0
        
        for i, num in enumerate(nums):
            # Case where num is not the first or last item in the nums list
            if (i) and ((i+1) < nums_length):
                if (nums[i-1] < nums[i] and nums[i+1] < nums[i]):
                    return i
            # Case where num is the first element in the nums list
            elif not (i):
                if (nums[i+1] < nums[i]):
                    return i
            # Case where num is the last element in the nums list
            elif (i+1) == nums_length:
                if (nums[i-1] < nums[i]):
                    return i
import sys


class Solution:
    """Leetcode https://leetcode.com/problems/maximum-subarray problem's solution"""

    def maxSubArray(self, nums: List[int]) -> int:
        """
        Finding the maximum subarray for given input array

        Returns:
            int: Maximum subarray for given input array
        """
        running_sum = 0  # current sum
        max_sum = 0  # maximum sum
        max_number = -sys.maxsize - 1  # max element in the list

        # iterate the input list
        for element in nums:
            # find maximum element in the input list
            if element > max_number:
                max_number = element

            # finding the maximum sub array - Greedy Approach
            running_sum += element
            running_sum = max(running_sum, element)
            max_sum = max(running_sum, max_sum)

        # if max element is negative then return that element
        if max_number < 0:
            return max_number

        return max_sum

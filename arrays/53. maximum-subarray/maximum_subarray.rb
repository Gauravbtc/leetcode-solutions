class Solution
  """Leetcode https://leetcode.com/problems/maximum-subarray problem's solution"""
  def maxSubArray(arr)
    # initailize max_end_hear and max_so_far hear with 0
    max_end_hear = max_so_far = 0

    arr.each do | a |
      max_end_hear += a
      if max_end_hear < 0
        ## element -ve then max_end_hear will be 0
        max_end_hear = 0
      end
      # update max_so_far whe max_end_hear is higer than max_so_far
      if max_end_hear > max_so_far
        max_so_far = max_end_hear
      end
    end
    max_so_far
  end
end

## Solution.new.maxSubArray([-2, -3, 4, -1, -2, 1, 5, -3])
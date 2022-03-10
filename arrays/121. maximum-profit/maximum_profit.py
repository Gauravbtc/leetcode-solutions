import sys


class Solution:
    """Leetcode https://leetcode.com/problems/best-time-to-buy-and-sell-stock/"""

    def maxProfit(self, prices: List[int]) -> int:
        max_sum = 0
        running_profit = 0
        min_ele = sys.maxsize
        for element in prices:
            running_profit = element - min_ele
            max_sum = max(running_profit, max_sum)
            if min_ele > element:
                min_ele = element

        return max_sum

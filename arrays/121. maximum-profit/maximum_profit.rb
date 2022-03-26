def max_profit(prices)
 len = prices.length
 max_diff = 0
 for i in 0 .. len - 1
   max_ele = prices[i..len].max
   ele_diff = max_ele - prices[i]
   if ele_diff > max_diff
     max_diff = ele_diff
   end
 end
 max_diff
end

## max_profit([7,1,5,3,6,4])
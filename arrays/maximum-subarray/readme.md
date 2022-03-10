# **Maximum sub array problem**

## **Problem**

### find the contiguous subarray (containing at least one number) which has the largest sum and return its sum. A **subarray** is a **contiguous** part of an array.

[Leet Code Link](https://leetcode.com/problems/maximum-subarray/)

#

## **Solution**

There two things we need to ask, while solving this problem.

1. Is there any negative number exist in the list?
2. Are all the numbers that exist in the list is negative?

### **Scenario 1**:

So first we will check whether maximum number of the input list/array is negative or not. if its a negative number then we got the answer for both the questions as **YES** and we need to return the maximum element as result.

```
    import sys
    max_number = -sys.maxsize - 1

    for element in nums:
        if element > max_number:
            max_number = element

    if max_number < 0:
        return max_number
```

### **Scenario 2**:

Now if the maximum number is not negative then we have to follow below three steps to find the maximum subarray sum from the list.

1. Calculate the **running sum** (continuos sum) of the list.
   ```
      running_sum += element
   ```
2. If the **running sum** is less then the **current element** then make the **current element** as **running sum**.
   ```
      running_sum = max(running_sum, element)
   ```
3. Find the **maximum sum** by comparing the **running sum** and **maximum sum**.
   ```
       max_sum = max(running_sum, max_sum)
   ```

and after iterating over all the elements we need to return the **maximum sum**.

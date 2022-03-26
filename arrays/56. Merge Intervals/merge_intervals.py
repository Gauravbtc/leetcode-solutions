class Solution:
    """Leetcode https://leetcode.com/problems/merge-intervals/ problem's solution"""

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = list()
        # sort the given list, sorted times are easy to calculate
        intervals.sort()

        for elements in intervals:
            # first element condition
            if len(result) < 1:
                result.append(elements)
            else:
                # take the previous time slot for comparision
                prev_element = result[-1]

                # if the current time slot can be included in previous time slot
                # then take the max
                if prev_element[1] >= elements[0]:
                    prev_element[1] = max(prev_element[1], elements[1])
                else:
                    # found new time slot
                    result.append(elements)

        return result

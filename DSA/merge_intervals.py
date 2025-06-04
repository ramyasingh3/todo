"""
Problem: Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    # If the input is empty or has only one interval, return as is
    if not intervals:
        return []
    if len(intervals) == 1:
        return intervals
    
    # Sort intervals based on start time
    intervals.sort(key=lambda x: x[0])
    
    merged = []
    current_interval = intervals[0]
    
    for interval in intervals[1:]:
        # If current interval overlaps with the next interval
        if current_interval[1] >= interval[0]:
            # Merge the intervals by updating the end time
            current_interval[1] = max(current_interval[1], interval[1])
        else:
            # No overlap, add current_interval to result and update current_interval
            merged.append(current_interval)
            current_interval = interval
    
    # Add the last interval
    merged.append(current_interval)
    return merged

# Test cases
def test_merge_intervals():
    # Test case 1: Regular overlapping intervals
    assert merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    
    # Test case 2: Intervals that touch
    assert merge([[1,4],[4,5]]) == [[1,5]]
    
    # Test case 3: No overlapping intervals
    assert merge([[1,2],[3,4],[5,6]]) == [[1,2],[3,4],[5,6]]
    
    # Test case 4: Complete overlap
    assert merge([[1,4],[2,3]]) == [[1,4]]
    
    # Test case 5: Single interval
    assert merge([[1,2]]) == [[1,2]]
    
    # Test case 6: Empty input
    assert merge([]) == []
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_merge_intervals() 
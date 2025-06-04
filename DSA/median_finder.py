import heapq

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Max heap for the lower half of numbers
        self.lower_half = []
        # Min heap for the upper half of numbers
        self.upper_half = []
        
    def addNum(self, num: int) -> None:
        """
        Add a number to the data structure.
        
        Args:
            num (int): Number to add
        """
        # If lower half is empty or num is smaller than max of lower half
        if not self.lower_half or num < -self.lower_half[0]:
            # Add to lower half (negated for max heap)
            heapq.heappush(self.lower_half, -num)
        else:
            # Add to upper half
            heapq.heappush(self.upper_half, num)
            
        # Balance the heaps
        if len(self.lower_half) > len(self.upper_half) + 1:
            # Move largest from lower to upper
            heapq.heappush(self.upper_half, -heapq.heappop(self.lower_half))
        elif len(self.upper_half) > len(self.lower_half):
            # Move smallest from upper to lower
            heapq.heappush(self.lower_half, -heapq.heappop(self.upper_half))
    
    def findMedian(self) -> float:
        """
        Return the median of current data stream.
        
        Returns:
            float: The median value
        """
        if len(self.lower_half) > len(self.upper_half):
            # If odd number of elements, median is max of lower half
            return -self.lower_half[0]
        else:
            # If even number of elements, median is average of both middle elements
            return (-self.lower_half[0] + self.upper_half[0]) / 2

# Test cases
def test_median_finder():
    # Example 1
    mf1 = MedianFinder()
    mf1.addNum(1)
    assert mf1.findMedian() == 1.0
    mf1.addNum(2)
    assert mf1.findMedian() == 1.5
    mf1.addNum(3)
    assert mf1.findMedian() == 2.0
    
    # Example 2
    mf2 = MedianFinder()
    mf2.addNum(2)
    assert mf2.findMedian() == 2.0
    mf2.addNum(3)
    assert mf2.findMedian() == 2.5
    
    # Additional test cases
    mf3 = MedianFinder()
    nums = [6, 10, 2, 6, 5, 0, 6, 3, 1, 0, 0]
    expected = [6.0, 8.0, 6.0, 6.0, 6.0, 5.5, 6.0, 5.5, 5.0, 4.0, 3.0]
    for num, exp in zip(nums, expected):
        mf3.addNum(num)
        assert abs(mf3.findMedian() - exp) < 1e-10
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_median_finder() 
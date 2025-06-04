# Find Median from Data Stream

## Problem Description
Design a data structure that supports the following two operations:
- `addNum(int num)`: Add an integer number from the data stream to the data structure.
- `findMedian()`: Return the median of all elements so far.

The median is the middle value in an ordered integer list. If the size of the list is even, the median is the average of the two middle values.

## Examples

### Example 1:
```
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.findMedian(); // return 1.0
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5
medianFinder.addNum(3);    // arr = [1, 2, 3]
medianFinder.findMedian(); // return 2.0
```

### Example 2:
```
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(2);    // arr = [2]
medianFinder.findMedian(); // return 2.0
medianFinder.addNum(3);    // arr = [2, 3]
medianFinder.findMedian(); // return 2.5
```

## Approach
The solution uses two heaps to efficiently maintain the running median:
1. A max heap for the lower half of the numbers
2. A min heap for the upper half of the numbers

Here's how it works:
1. When adding a number:
   - If the number is smaller than the max of lower half, add to lower half
   - Otherwise, add to upper half
   - Balance the heaps so their sizes differ by at most 1
2. When finding the median:
   - If heaps have equal size, return average of their tops
   - Otherwise, return top of the larger heap

## Time Complexity
- addNum: O(log n)
  - Heap insertions and balancing take logarithmic time
- findMedian: O(1)
  - Just peek at the top elements of the heaps

## Space Complexity
- O(n), where n is the number of elements in the data stream
- We store all elements across two heaps

## Solution Code
The solution is implemented in `median_finder.py`. 
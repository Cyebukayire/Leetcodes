# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The first aim is to find a pair of two same numbers in the input array. 
When pair is found, then we check if product of their indices is divisible by k

# Approach
<!-- Describe your approach to solving the problem. -->
I utilized a dictionary to help store all occurances of each number, so I easily can access any repeated element and it's index in the array **nums**
# Complexity
- Time complexity: O(N)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:O(N)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
from collections import defaultdict
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        seen = defaultdict(list)
        count = 0
        for i, num in enumerate(nums):
            if num in seen:
                # A good pair is found: check requirements  
                count += sum([1 if ((idx*i) % k) == 0 else 0 for idx in seen[num]])
            seen[num].append(i)

        return count
```

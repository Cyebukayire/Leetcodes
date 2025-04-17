# Intuition
The goal is to count all pairs of indices `(i, j)` where `i < j`, `nums[i] == nums[j]`, and the product `i * j` is divisible by `k`.

# Approach
I used a `defaultdict` to keep track of all the indices where each number appears in the array. When encountering a number that has already appeared before, I iterate through its previous indices to check if the condition `(i * j) % k == 0` holds.

# Complexity
- Time complexity: O(N) 
- Space complexity: O(N)

# Code
```python
from collections import defaultdict

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        seen = defaultdict(list)
        count = 0
        for i, num in enumerate(nums):
            for idx in seen[num]:
                if (i * idx) % k == 0:
                    count += 1
            seen[num].append(i)
        return count

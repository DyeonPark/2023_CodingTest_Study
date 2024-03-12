"""
Given a collection of numbers, nums, that might contain duplicates, 
return all possible unique permutations in any order.

Input: nums = [1,1,2]
Output:
[[1,1,2], [1,2,1], [2,1,1]]

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        print()
        result = []
        dp = set()
        # print(nums, dp)
        if len(nums) == 1: return [nums[:]] 

        for i in range(len(nums)):
            n = nums.pop(0)
            if (n, len(nums)) not in dp: 
                perms = self.permuteUnique(nums)
                dp.add((n, len(nums)))
                print(n, perms, dp)
                for p in perms: p.append(n)
                print(perms)
                result.extend(perms)
            nums.append(n)

        return result


# ans = Solution().permuteUnique([1,2,3]); print(ans)
ans = Solution().permuteUnique([1,1,3]); print(ans)

"""



1 [[3]]                {(1, 1)}
[[3, 1]]

3 [[1]]                {(3, 1), (1, 1)}
[[1, 3]]
1 [[3, 1], [1, 3]]     {(1, 2)}
[[3, 1, 1], [1, 3, 1]]

                       (1, 2) already in dp

3 [[1]]                {(3, 1), (1, 2)}
[[1, 3]]
[[3, 1, 1], [1, 3, 1], [1, 3]]
"""

"""

1 [[3]]
[[3, 1]]

3 [[1]]
[[1, 3]]

1 [[3, 1], [1, 3]]
[[3, 1, 1], [1, 3, 1]]



3 [[1]]
[[1, 3]]

1 [[3]]
[[3, 1]]

1 [[1, 3], [3, 1]]
[[1, 3, 1], [3, 1, 1]]



1 [[1]]
[[1, 1]]

1 [[1]]
[[1, 1]]

3 [[1, 1], [1, 1]]
[[1, 1, 3], [1, 1, 3]]

[[3, 1, 1], [1, 3, 1], [1, 3, 1], [3, 1, 1], [1, 1, 3], [1, 1, 3]]
"""
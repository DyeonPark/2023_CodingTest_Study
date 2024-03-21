from typing import List
"""
nums = [1,2,2] -> [[],[1],[1,2],[1,2,2],[2],[2,2]]
nums = [0] -> [[],[0]]
"""

class Solution:
    def subsetsWithDup_ii(self, nums: List[int]) -> List[List[int]]:
        """
        recursion step
            - append the current subset `ds` to the result list
            - iterate over the remaining elements of nums, starting from the given index `idx`.
                - checks1. if its the first occurrence of that number
                - checks2. whether its the same as the previous element
                - both true) 
                    - skip the current element to avoid duplicate
                - ow) 
                    - include the current element in the subset
                    - recursion(updated subset, index)
                    - remove the last element from the subset(=backtrack)
                    - explore other possibilities
        """
        def backtrack_ii(idx: int, ds: List[int]):
            print(idx, ds, result)
            result.append(ds[:])
            for i in range(idx, len(nums)):
                if i != idx and nums[i] == nums[i-1]: continue
                ds.append(nums[i])
                backtrack_ii(i+1, ds)
                ds.pop()

        result = []
        backtrack_ii(0, [])
        return result



    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i: int, nums: List[int], subset: List[int]):
            """
            base case : i is the end index of the nums
            backtrack(take nums[i])
            backtrack(not take nums[i])
            - if its not decided to not taking the nums[i], not taking the entire step
            """
            if i == len(nums): 
                result.append(subset[:])
                return
            # not take nums[i] - would not take nums[i] in this -> give i+(num of nums[i])
            j = i 
            while j < len(nums) and nums[i] == nums[j]: 
                j+=1
            backtrack(j, nums, subset)
            # take nums[i] - take 
            subset.append(nums[i])
            backtrack(i+1, nums, subset)
            subset.pop()
            return

        result = []
        nums = sorted(nums)
        backtrack(0, nums, [])
        return result
    
ans = Solution().subsetsWithDup_ii([1, 2, 2]); print(ans)
ans = Solution().subsetsWithDup_ii([0]); print(ans)
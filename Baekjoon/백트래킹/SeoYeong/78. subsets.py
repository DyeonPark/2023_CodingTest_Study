"""
nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        def solve(
            - i : index of the current element in nums
            - nums : input array
            = subset : current subset being constructed
        ): 
            base case
            - when i becomes the size of the nums, it means that we have processed
            all elements of nums. The current subset is a valid subset, so add it to the result list.
            
            recursively generates subsets by considering two choices
            - whether to include the current element nums[i]
            - not take
                - recursively call solve(i+1, nums, subset)
            - take
                - push nums[i] into the subset
                - recursively call solve(i+1, nums, subset)
                - pop the last element from the subset to backtrack and explore other possibilities

        """
        def backtrack(i, nums, subset):
            if i == len(nums): 
                result.append(subset[:])
                return 
            backtrack(i+1, nums, subset)
            subset.append(nums[i])
            backtrack(i+1, nums, subset)
            subset.pop()


        result = []
        backtrack(0, nums, [])
        return result
    



    def subsets_firstTry(self, nums: List[int]) -> List[List[int]]:
        def backtracking(nums):
            print(nums)
            result = [nums[:]]

            if len(nums) == 1: return result

            for _ in range(len(nums)):
                n = nums.pop(0)
                ss = backtracking(nums)
                print(ss)
                # for s in ss: s.append(n)
                # print(ss)
                for s in ss: 
                    if s not in result: result.append(s)
                nums.append(n)

            return sorted(result)
    
        ans = backtracking(nums)
        ans.append([])
        return sorted(ans, key=len)


        
    
    
ans = Solution().subsets([1, 2, 3]); print(ans)
            
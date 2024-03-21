"""
진짜 레전드 개뻘짓했네 ㄷ ㄷ ㄷ ㄷ
[1][2][3][1, 2][2,3][1,3][1,2,3] 이걸 구하는게 아니라
[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
이걸 구하는 거였음 ㄷ ㄷ ㄷ ㄷ ㄷ ㄷ ㄷㄷㄷ ㄷ ㄷ ㄷ ㄷ ㄷ ㄷ


return all possible permutations
                   [1,2,3]
     [2, 3]         [1, 3]         [1, 2]
    [2]    [3]    [1]    [3]      [1]   [2]

- list of result
- base case : length of array is 1 -> list of list
- iterate through the range of the length of the array
    - pop out the first index of value
    - get the perm list recusively
    - iterate through the perm 
"""

from typing import List


class Solution1:
    def permute(self, nums: List[int], depth: int) -> List[List[int]]:
        # print(f"\n{' '*depth}permute({nums})")
        ans = [nums[:]]
        if len(nums) <= 1: 
            # print(f"{'  '*depth}return {nums}")
            return [nums.copy()]

        for i in range(len(nums)):
            n = nums.pop(0)

            perms = self.permute(nums, depth+1)
            # print(f"{'  '*depth}perms : {perms}")
            if perms not in ans: ans.extend(perms)
            nums.append(n)
            
        # print(f"{'  '*depth}ans : {ans}")
        return ans


class Solution:
    """
    [1,2,3] -[2,3] - 
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) == 1: return [nums[:]]

        for _ in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for p in perms:
                p.append(n)
            nums.append(n)
            result.extend(perms)
        return result


ans = Solution().permute([1, 2 ,3]); print(ans)



class Solution:
    def permute(self, nums):
        ans = []
        def reursive(lst):
            print(lst)
            # base case = nums가 1개짜리 원소면 nums 리턴
            if len(lst) == 1: return [lst.copy()]

            # nums 돌면서 하나씩 pop해서 resursive permute 보내고, 받은거 result에 넣고 pop 한거 nums에 다시 넣고 result 리턴 
            for i in range(len(lst)):
                n = lst.pop(0)
                perm = reursive(lst)
                ans.append(perm)
                lst.append(n)

            print(ans)
            return [lst]
        reursive(nums)
         


"""
[[[2], [1, 2]], [[1], [1, 2]]]
[[[[3], [1, 2, 3]], [[2], [1, 2, 3]], [1, 2, 3]], [[[1], [1, 2, 3]], [[3], [1, 2, 3]], [1, 2, 3]], [[[2], [1, 2, 3]], [[1], [1, 2, 3]], [1, 2, 3]]]
지금 그냥 base case에서 nums 만 반복적으로 단순 뒤에 붙어서 리턴되곡 있으ㅜㅂㅁ

"""

# ans = Solution1().permute([1, 2, 3], 0); print(ans)



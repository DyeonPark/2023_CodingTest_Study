"""
partition s 
- every substring of the partition is palindrome
- return all possible palindrome paritioning of s
- substring : contiguous non-empty substring
"""
from typing import List


class Solution:
    def is_palinrome(self, s: str) ->bool:
        l, r = 0, len(s)-1
        while l<r:
            if s[l] != s[r]: return False
            l+=1; r-=1
        return True
        
    def partition(self, s: str) -> List[List[str]]:
        result = []
        subset = []

        def dfs(i: int):
            if i >= len(s):
                # print(f"subset: {subset}. return")
                result.append(subset.copy())
                return
            
            for j in range(i, len(s)):
                current_substring = s[i:j+1]
                if self.is_palinrome(current_substring):
                    subset.append(current_substring)
                    dfs(j+1)
                    subset.pop()
        
        dfs(0)
        return result

    def partition_(self, s: str) -> List[List[str]]:
        """
        branch condition : 
        - branch every single possible way we could partitioned
        - check if that partition form palindromes
        """
        result = [[st for st in s]]
        dp = set()
        for gap in range(1, len(s)):
            for i in range(len(s)-gap):
                partitioned = s[i:i+gap+1]
                if partitioned not in dp and is_palinrome(partitioned):
                    dp.add(partitioned)

        print(dp)

Solution().partition("aab")
# Solution().partition("a")
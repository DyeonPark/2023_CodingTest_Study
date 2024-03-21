
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        dic = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        result = []
        tmp = []
        def dfs(i: int):
            if i == len(digits):
                result.append(''.join(tmp))
                return
            
            for x in dic[digits[i]]:
                tmp.append(x)
                dfs(i+1)
                tmp.pop()

        dfs(0)
        return result


Solution().letterCombinations('23')
Solution().letterCombinations('')
Solution().letterCombinations('2')

        
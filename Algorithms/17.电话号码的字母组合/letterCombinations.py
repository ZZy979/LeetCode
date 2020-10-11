class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        key = {
            '2': 'abc', '3': 'def',
            '4': 'ghi', '5': 'jkl', '6': 'mno',
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        if not digits:
            return []
        ans = ['']
        for d in digits:
            ans = [pre + suf for pre in ans for suf in key[d]]
        return ans

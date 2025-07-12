# Last updated: 7/12/2025, 6:59:09 PM
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        my_dict= {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        if not digits:
            return []

        result=[]

        def backtrack(index, path):
            if index== len(digits):
                result.append(path[:])
                return

            for char in my_dict[digits[index]]:
                backtrack(index+1, path+char)

        backtrack(0, "")
        return result
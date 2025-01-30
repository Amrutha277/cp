class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        total_map= {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        result=[]
        if not digits:
            return []
        def helper(index, curr_set):
            if index==len(digits):
                result.append(''.join(curr_set))
                return

            for letter in total_map[digits[index]]:
                curr_set.append(letter)
                helper(index+1, curr_set)
                curr_set.pop()
            
        helper(0,[])
        return result

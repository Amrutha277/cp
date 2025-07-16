# Last updated: 7/15/2025, 9:28:37 PM
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen=[]
        
        def helper(r, c, i):
            if i == len(word):
                return True
            if r<0 or c<0 or r>= len(board) or c>= len(board[0]) or board[r][c] != word[i]:
                return False

            temp= board[r][c]
            board[r][c]= '#'

            found= (
                helper(r+1, c, i+1) or
                helper(r-1, c, i+1) or
                helper(r, c-1, i+1) or
                helper(r, c+1, i+1)
                )

            board[r][c] =temp
            return found

        for r in range(len(board)):
            for c in range(len(board[0])):
                if helper(r, c, 0):
                    return True
        return False

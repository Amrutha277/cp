# Last updated: 11/5/2025, 10:30:10 AM
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
       """
        num_rows, num_cols = len(board), len(board[0])

        neighbor_dir=[
            (-1,-1), (-1,0),(-1,1),
            (0,-1),         (0,1),
            (1,-1),(1,0),(1,1)
        ]

        for row in range(num_rows):
            for col in range(num_cols):
                live_neighbor_count =0

                for row_offset, col_offset in neighbor_dir:
                    neighbor_row = row + row_offset
                    neighbor_col = col + col_offset

                    if(
                        0 <= neighbor_row < num_rows and
                        0 <= neighbor_col < num_cols and
                        abs(board[neighbor_row][neighbor_col]) == 1
                    ):
                        live_neighbor_count +=1
                if board[row][col] ==1:
                    if live_neighbor_count <2 or live_neighbor_count >3:
                        board[row][col] = -1
                
                if board[row][col] == 0:
                    if live_neighbor_count == 3:
                        board[row][col] = 2
        
        for row in range(num_rows):
            for col in range(num_cols):
                if board[row][col] == -1:
                    board[row][col] = 0
                elif board[row][col] == 2:
                    board[row][col] = 1


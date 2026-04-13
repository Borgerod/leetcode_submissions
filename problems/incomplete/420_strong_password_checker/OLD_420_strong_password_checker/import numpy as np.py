from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # board = np.array(board)
        # sublists = np.concatenate([board, self.get_cols(board), self.get_boxes(board)], axis=0)
        sublists = board + self.get_cols(board) + self.get_boxes(board)
        for sublist in sublists:
            checked = set()
            for val in sublist:
                if val != '.' and val in checked:
                    return False
                checked.add(val)
        
        return True
    

    def get_cols(self, board):
        all_cols = []
        for i in range(0,9):
            col = []
            for row in board:
                col.append(row[i])
            all_cols.append(col)
        return all_cols

    def get_boxes(self, board):
        iteration_keys = [[1,2,3],[1,2,3],[1,2,3], [4,5,6],[4,5,6],[4,5,6], [7,8,9],[7,8,9],[7,8,9],]
        mp = defaultdict(list)
        for row, key_section in zip(board, iteration_keys):
            mp[key_section[0]].extend(row[0:3])
            mp[key_section[1]].extend(row[3:6])
            mp[key_section[2]].extend(row[6:9])
        return [mp.get(i) for i in mp] 
    

test_cases = [
[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]],
[["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]],
[[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]],
]
for i, board in enumerate(test_cases): 
    s = Solution()
    res = s.isValidSudoku(board)
    print(f"results for case [{i}] : {res}")
    print("_"*50,"\n")

    
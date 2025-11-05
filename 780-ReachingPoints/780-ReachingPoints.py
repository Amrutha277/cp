# Last updated: 11/5/2025, 4:27:50 PM
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if sx == tx and sy == ty:
            return True
        while tx>sx and ty>sy:
            if tx>ty:
                tx %= ty
            else:
                ty %= tx
        if tx == sx:
            return (ty-sy)%sx == 0 and ty>sy
        
        if ty == sy:
            return (tx-sx)%sy == 0 and tx > sx
        return False



        
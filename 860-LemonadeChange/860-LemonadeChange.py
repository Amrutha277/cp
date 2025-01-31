class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        curr_val=0
        num5, num10, num20=0,0,0
        for i in range(len(bills)):
            # print(curr_val)
            if bills[i]==5:
                num5+=1
            elif bills[i]==10:
                # print("in if")
                if num5>=1:
                    num10+=1
                    num5-=1
                else:
                    return False
            elif bills[i]==20:
                if num10>=1 and num5>=1:
                    num20+=1
                    num5-=1
                    num10-=1
                elif num5 >=3:
                    num20+=1
                    num5-=3
                else:
                    return False                                
        return True


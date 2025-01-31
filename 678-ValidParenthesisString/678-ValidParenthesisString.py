class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_bal, right_bal=0,0
        for char in s:
            if char == '(' or char == '*':
                left_bal += 1
            else:
                left_bal -= 1
            if left_bal < 0:
                return False  # Too many ')'

        
        for char in reversed(s):
            if char == ')' or char == '*':
                right_bal += 1
            else:
                right_bal -= 1
            if right_bal < 0:
                return False  # Too many '('

        return True


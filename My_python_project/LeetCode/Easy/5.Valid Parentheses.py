class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        balanced = True
        index = 0
        while index < len(s) and balanced:
            par = s[index]
            if par in "([{":
                stack.append(par)
            else:
                if len(stack) == 0:
                    balanced = False
                else:
                    top = stack.pop()
                    if not Solution.match(self, top, par):
                        return False
            index += 1
        if balanced and len(stack) == 0:
            return True
        else:
            return False
    def match(self, open, close):
        opens = "([{"
        closes = ")]}"
        return opens.index(open) == closes.index(close)

""" 
case: ((({{]],  (){}[],  {[()]}, 
"""
sol = Solution()
print(sol.isValid("((({{]]"))
class Solution(object):
    def isValid(self, s):
        list_str = list(s)
        dic_element = {'(':1, ")":-1, "[":2, "]":-2, "{":3, "}":-3}
        if len(list_str)%2 != 0:
            return False
        elif dic_element[list_str[0]] < 0:
            return False
        elif dic_element[list_str[len(list_str)]] > 0:
            return False
        else:
            count = 0
            for i in range(0, len(list_str) - 1):
                for j in range(i+1, len(list_str)):
                    if dic_element[list_str[i]] + dic_element[list_str[j]] != 0:
                        continue
                    else:




        return
"""
case: ((({{]],  (){}[],  {[()]}, 
"""
sol = Solution()
print(sol.isValid("({})"))
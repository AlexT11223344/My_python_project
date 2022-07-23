class Solution(object):
    def isValid(self, s):
        list_str = list(s)
        dic_element = {'(':1, ")":-1, "[":2, "]":-2, "{":3, "}":-3}
        if len(list_str)%2 != 0 or dic_element[list_str[len(list_str)]] > 0 or dic_element[list_str[0]] < 0:
            return False
        else:
            count_pos = 0
            count_neg = 0
            for i in range(0, len(list_str)):
                if list_str[i] > 0:
                    count_pos += 1
                else:
                    count_neg += 1
            if count_pos != count_neg:
                return False
            else:





        return
"""
case: ((({{]],  (){}[],  {[()]}, 
"""
sol = Solution()
print(sol.isValid("({})"))
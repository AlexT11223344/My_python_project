class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_list = list(s.split(" "))
        if s == "":
            return 0
        else:
            new_list = []
            for i in s_list:
                if i != '':
                    new_list.append(i)
            last_index = len(new_list) - 1
            return len(new_list[last_index])
str = "hello"
needle = "ll"

# Solution 1
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        haystack = list(haystack)
        # needle = list(needle)

        m = len(haystack)
        n = len(needle)
        flag = False

        if n == 0 or n > m:
            return -1
        else:
            for i in range(0, m):
                if i + n <= m:
                    temp = haystack[i:i + n]
                    temp = ''.join(temp)
                    if temp == needle:
                        flag = True
                        return i
                else:
                    return -1
            if flag == False:
                return -1
# Solution 2

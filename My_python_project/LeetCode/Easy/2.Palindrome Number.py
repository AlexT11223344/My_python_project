class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0:
            a = [int(j) for j in str(x)]
            boundry = int(0.5 * len(a))
            for i in range(0, boundry):
                opposite = len(a) - 1 - i
                if a[i] == a[opposite]:
                    continue
                else:
                    return False
            return True
        else:
            return False
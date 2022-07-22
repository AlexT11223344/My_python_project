class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        i = 0
        _sum = 0

        while i < len(s):
            _IV = 0
            _IX = 0
            _XL = 0
            _XC = 0
            _CD = 0
            _CM = 0

            if i == len(s) - 1:
                pass

            elif s[i] == 'I':

                if s[i + 1] == 'V':
                    _IV = 4
                elif s[i + 1] == 'X':
                    _IX = 9
                else:
                    pass

            elif s[i] == 'X':

                if s[i + 1] == 'L':
                    _XL = 40
                elif s[i + 1] == 'C':
                    _XC = 90
                else:
                    pass

            elif s[i] == 'C':

                if s[i + 1] == 'D':
                    _CD = 400
                elif s[i + 1] == 'M':
                    _CM = 900
                else:
                    pass

            if i == len(s) - 1:
                _sum += dic[s[i]]
                break
            elif _IV != 0 or _IX != 0 or _XL != 0 or _XC != 0 or _CD != 0 or _CM != 0:
                _sum += _IV + _IX + _XL + _XC + _CD + _CM
                i += 2
            else:
                _sum += dic[s[i]]
                i += 1

        return _sum

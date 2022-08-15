class Solution:
    def mySqrt(self, x: int) -> int:
        x_previous = x
        x_current = x / 2
        precision = 0.1
        while abs(x_previous - x_current) > precision:
            x_previous = x_current
            x_current = (1 / 2) * (x_current + x / x_current)

        return int(x_current)
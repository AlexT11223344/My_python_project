class Solution:
    def addBinary(self, a: str, b: str) -> str:

        a = list(a)
        b = list(b)

        list_int_a = [int(x) for x in a]
        list_int_b = [int(x) for x in b]

        sum_a = 0
        sum_b = 0

        for i in range(0, len(list_int_a)):
            if list_int_a[len(list_int_a) - i - 1] == 1:
                sum_a += pow(2, i)
            else:
                continue

        for j in range(0, len(list_int_b)):
            if list_int_b[len(list_int_b) - j - 1] == 1:
                sum_b += pow(2, j)
            else:
                continue

        sum_total = sum_a + sum_b
        sum_total_bin = bin(sum_total).replace('0b', '')
        return str(sum_total_bin)
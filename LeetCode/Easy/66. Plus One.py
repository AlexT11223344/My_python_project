class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = [str(x) for x in digits]
        number = int(''.join(number))
        number = number + 1
        number = list(str(number))
        return number
class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        minimal = min(A)
        res = 0
        for digit in str(minimal):
            res += int(digit)
        if res%2 == 0:
            return 1
        else:
            return 0
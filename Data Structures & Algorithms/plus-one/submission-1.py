class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        rem = 0
        quo = 1
        for i in range(len(digits)):
            cur = digits[i] + quo
            quo = cur // 10
            rem = cur % 10
            digits[i] = rem
        if quo > 0:
            digits.append(quo)

        digits.reverse()
        return digits
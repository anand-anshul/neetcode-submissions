class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        carry = 0
        digits[-1] += 1

        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            
            rem = digits[i] % 10
            carry = digits[i] // 10
            res.append(rem)
        if carry:
            res.append(carry)

        return res[::-1]

             

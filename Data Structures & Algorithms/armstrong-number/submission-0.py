class Solution:
    def isArmstrong(self, n: int) -> bool:
        k = 0
        armst = 0
        test = n
        arr = []
        while n > 0:
            rem = n % 10
            n = n // 10
            arr.append(rem)

        for num in arr:
            armst += num ** len(arr)

        return armst == test  
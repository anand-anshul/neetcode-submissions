class Solution:
    def countBits(self, n: int) -> List[int]:
        def hamming(x):
            count = 0

            while x > 0:
                count += x & 1

                x = x >> 1

            return count

        res = []

        for i in range(n + 1):
            res.append(hamming(i))

        return res

    
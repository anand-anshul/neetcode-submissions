class Solution:
    def maxScore(self, s: str) -> int:
        zero_prefix = [0] * len(s)
        one_prefix = [0] * len(s)

        zero_cur = 0
        one_cur = 0
        for i in range(len(s)):
            if s[i] == "0":
                zero_cur += 1
            zero_prefix[i] = zero_cur

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "1":
                one_cur += 1
            one_prefix[i] = one_cur
            

        max_score = 0
        cur_score = 0

        for i in range(len(s) - 1):
            cur_score = zero_prefix[i] + one_prefix[i + 1]
            max_score = max(max_score, cur_score)

        return max_score


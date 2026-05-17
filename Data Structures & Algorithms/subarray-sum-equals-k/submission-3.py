class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = cur_sum = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1

        for num in nums:
            cur_sum += num

            difference = cur_sum - k

            res += prefix_sums[difference]
            prefix_sums[cur_sum] += 1

        return res


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count_1 = Counter(s1)
        left = 0

        count_2 = defaultdict(int)

        for right in range(len(s2)):
            r_char = s2[right]
            count_2[r_char] += 1

            while left < len(s2) and (right - left + 1) > len(s1):
                l_char = s2[left]
                count_2[l_char] -= 1
                if count_2[l_char] == 0:
                    del count_2[l_char]
                left += 1

            if count_1 == count_2:
                return True

        return False


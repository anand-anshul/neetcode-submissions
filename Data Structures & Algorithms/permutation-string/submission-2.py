class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count_1 = defaultdict(int)
        for c in s1:
            count_1[c] += 1

        count_2 = defaultdict(int)
        left = 0
        for right in range(len(s2)):
            char = s2[right]
            count_2[char] += 1
            
            if right - left + 1 > len(s1):
                left_char = s2[left]
                count_2[left_char] -= 1
                if count_2[left_char] == 0:
                    del count_2[left_char]
                left += 1
            
            if count_1 == count_2:
                return True
            
            right += 1
        return False

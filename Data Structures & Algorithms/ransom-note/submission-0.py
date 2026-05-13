class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        ran_count = defaultdict(int)
        mag_count = defaultdict(int)

        for c in ransomNote:
            ran_count[c] += 1

        for c in magazine:
            mag_count[c] += 1

        for c, n in ran_count.items():
            if c not in mag_count or mag_count[c] < n:
                return False
        return True
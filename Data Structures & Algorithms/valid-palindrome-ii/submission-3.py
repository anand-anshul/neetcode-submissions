class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s):
            left = 0
            right = len(s) - 1

            while left < right:
                while left < right and not s[left].isalnum():
                    left += 1
                while left < right and not s[right].isalnum():
                    right -= 1

                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1

            else:
                return (
                    isPalindrome(s[left : right]) or
                    isPalindrome(s[left+1 : right+1])
                )

        return True
                
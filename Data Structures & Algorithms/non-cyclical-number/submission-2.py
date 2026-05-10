class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next_num(x):
            next_num = 0

            while x > 0:
                digit = x % 10
                x = x // 10

                next_num += digit ** 2

            return next_num

        slow = fast = n

        while True:
            slow = get_next_num(slow)
            fast = get_next_num(get_next_num(fast))

            if fast == 1:
                return True

            if slow == fast:
                return False 

    
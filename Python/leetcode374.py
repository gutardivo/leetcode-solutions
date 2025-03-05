def guess(n):
    pick = 6
    if n > pick:
        return -1
    elif n < pick:
        return 1
    elif n == pick:
        return 0
    
class Solution:
    def guessNumber(self, n: int) -> int:
        if guess(n) == 0:
            return n
        
        l, r = 0, n
        m = n

        while l < r:
            m = (l+r) // 2

            if guess(m) == 1:
                l = m
            elif guess(m) == -1:
                r = m
            else:
                return m


print(Solution().guessNumber(10))
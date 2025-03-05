class Solution:
    def __init__(self):
        self.memo = {0: 0, 1: 1}  # Base cases for Fibonacci
    
    def fib(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]  # Return memoized result
        
        self.memo[n] = self.fib(n - 1) + self.fib(n - 2)  # Recursive call with memoization
        return self.memo[n]


print(Solution().fib(3))
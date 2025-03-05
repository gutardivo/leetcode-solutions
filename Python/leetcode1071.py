def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if str1 and str2 have a common repeating pattern
        if str1 + str2 != str2 + str1:
            return ""
        
        # Compute GCD of the lengths
        gcd_length = gcd(len(str1), len(str2))
        
        # Return the substring of length gcd_length
        return str1[:gcd_length]

s = Solution()
test1 = "ABCABC"
test2 = "ABC"
test3 = "ABABAB"
test4 = "ABAB"
test5 = "LEET"
test6 = "CODE"

print(s.gcdOfStrings(test1,test2))
print(s.gcdOfStrings(test3,test4))
# print(s.gcdOfStrings(test5,test6))
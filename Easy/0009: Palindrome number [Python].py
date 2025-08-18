# Complexity: O(n)

class Solution(object):
    def isPalindrome(self, x):
        
        x = str(x)

        y = x[::-1] # Reversing the string
        
        if x == y: return True
        else: return False

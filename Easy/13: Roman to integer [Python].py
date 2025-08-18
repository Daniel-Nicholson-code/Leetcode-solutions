# Complexity: O(n)

class Solution(object):
    def romanToInt(self, s):
    
        dictionary = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000 }
        
        total = 0

        for i, letter in enumerate(s):
            value = dictionary[letter]

            # Case if the following letter has larger value
            if i != (len(s)-1):
                if value < dictionary[s[i+1]]:
                    total -= 2*value
  
            total += value

        return total

# Complexity: O(n)

class Solution(object):
    def isValid(self, s):
        
        # Skipping computation in special case
        if len(s) == 1: return False

        dictionary = {")":"(",
                    "}":"{",
                    "]":"["}

        stack = []
        for bracket in s:

            # If right bracket
            if bracket in dictionary.keys():
                if (not stack) or (dictionary[bracket] != stack.pop()):
                    return False

            # If left bracket
            elif bracket in dictionary.values():
                stack.append(bracket)

        return (not stack)

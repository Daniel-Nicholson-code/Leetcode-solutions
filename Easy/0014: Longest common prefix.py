# Complexity O(nm)
# Where n is the length of strs and m is the length of the prefix

class Solution(object):
    def longestCommonPrefix(self, strs):
        
        # Edge case to skip comptutation
        if len(strs) == 1: return strs[0]

        # Finding the minimum length of the elements of strs
        # We are told each length is <= 200 and >= 0
        minWordLength = 200
        for word in strs:
            if len(word) < minWordLength:
                minWordLength = len(word)

        # Edge case to skip comptutation
        if minWordLength == 0: return ""

        # Finding the longest common prefix
        prefix = ""
        done = False
        for i in range(minWordLength):

            letter = strs[0][i]
            
            # Checking if each element of strs has the same
            # letter at index i
            for j in range(len(strs)):
                if letter != strs[j][i]:
                    done = True
                    break

            if done: break
            else: prefix += letter
        
        return prefix

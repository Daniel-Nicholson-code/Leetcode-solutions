# Complexity: O(n)

class Solution(object):
    def twoSum(self, nums, target):
        
        index = [0, 0]
        hashmap = {}

        for i in range(len(nums)):

            value = nums[i]

            if target - value in hashmap:
                index = [i, hashmap[target - value]]
                break
            
            hashmap[value] = i
                
        return index

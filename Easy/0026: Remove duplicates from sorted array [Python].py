# Complexity: O(n)

class Solution(object):
    def removeDuplicates(self, nums):

        filter = [nums[0]]

        for i in range(1,len(nums)):

            if nums[i] != nums[i-1]:
                filter.append(nums[i])

        # Normal assignment doesn't work, not sure why
        nums[:] = filter[:]

        return len(filter)

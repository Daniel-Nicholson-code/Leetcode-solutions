# Complexity: O(n+m)
# where n+m is the sum of the lengths of list1 and list 2

class Solution(object):
    def mergeTwoLists(self, list1, list2):

        # Create a new list and the head of it
        merge = item = ListNode()

        # Repeat until all of the items in one of lists have been
        # exhausted
        while (list1 is not None) and (list2 is not None):

            # Add the smallest value to the merged list
            if list1.val < list2.val:
                item.next = list1
                list1 = list1.next
            else:
                item.next = list2
                list2 = list2.next

            # Increment the counter
            item = item.next

        # Once reached the end of one of the lists, add the other list on
        # to the merged list
        item.next = list1 or list2
        
        return merge.next

"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions

Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]
 

Constraints:
> The number of nodes in the list is in the range [0, 200].
> -100 <= Node.val <= 100
> -200 <= x <= 200
"""

# THOUGHTS
# NOT me getting stuck because I thought the directions said to put all the nodes greater than x after the node with value x... I was so confused about why 4 came before 3 in example 1. KARL, pls read the directions!
# Besides that, this problem wasn't too bad since I quickly realized it could be solved using the pointer approach. 
# I noticed that I tend to overthink these problems, and my code reflects that because my code at the beginning tends to be unnecessarily complicated. 
# Nevertheless, I was able to cut my code to what's below after refactoring and getting rid of the convolutions I noticed. 

# ------------- ATTEMPT 1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
    """
    Partitions a nodelist such that all of the nodes with values less than x come before all the nodes with values greater than or equal to x

    Has O(n) time complexity, where n is the number of nodes, since the loop only goes through each node in the nodelist once. 

    O(1) space complexity because I'm only using 5 variables to store important locations in each list.
    """
        # Check that there are elements in the list
        if not head:
            return head
        
        # Using the pointer method to keep track of two lists: list of nodes with values less than x and list of nodes with values greater or equal to x
        ptr = head
        less_head = ListNode(0)
        less = less_head
        great_or_equal_head = ListNode(0)
        great_or_equal = great_or_equal_head

        while ptr != None:
            if ptr.val < x:
                less.next = ptr
                less = ptr
            elif ptr.val >= x:
                great_or_equal.next = ptr  
                great_or_equal = ptr
            ptr = ptr.next
        
        # Append the nodes with values greater or equal to x to the end of the list of nodes with values less than x
        less.next = great_or_equal_head.next
        # Set end of greater or equal to nodelist to None to prevent cycles
        great_or_equal.next = None
    
        # Returns less_head.next because less_head = ListNode(0)
        return less_head.next
"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Constraints:

- The relative order inside both the even and odd groups should remain as it was in the input.
- The first node is considered odd, the second node even and so on ...
- The length of the linked list is between [0, 10^4].
"""

# THOUGHTS:
# Make sure to consider edge cases! I didn't think about the edge case where the given list is empty, which caused a Runtime Error.
# I saved some memory from my original code by deleting the odd_head variable; head IS the odd list head.
# It is O(n) space complexity because odd and even combined go through all elements of the list at most one time.
# It is O(1) space complexity because I am only keeping track of the four pointers: head, even_head, odd, and even.
# I am also trying to make my code follow style conventions as much as possible, which is why I am using snake_case for the function and variable names.

# ---------------------------- ACTUAL CODE BELOW 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def create_odd_even_list(self, head: ListNode) -> ListNode:
        """
        Using a four pointer approach, groups all elements in odd places in the given list 
        followed by the elements in even places with O(1) space and O(n) time complexity
        """
        
        # Checks if the provided linked list is empty and returns if it is
        if not head:
            return head
    
        # Head of even list; head of odd list is already defined
        even_head = head.next
        # Iterators
        odd = head
        even = even_head
        
        # Groups all elements in odd places in the list together; same for elements in even places 
        while (odd.next != None) and (even.next != None):
            odd.next = even.next
            odd = odd.next
            
            even.next = odd.next
            even = even.next
            
        # Appends the even list to the end of the odd list
        odd.next = even_head
        
        return head
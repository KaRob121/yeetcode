"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Constraints:

- The relative order inside both the even and odd groups should remain as it was in the input.
- The first node is considered odd, the second node even and so on ...
- The length of the linked list is between [0, 10^4].
"""

// THOUGHTS
// This implementation is pretty much the same as the Python3 one, running in O(n) time and with O(1) space complexity.
// However, this implementation uses real pointers, as is the magic of C++.
// One thing that I was confused about was whether or not I need to allocated memory and then deallocate it, but I realized that I didn't because I wasn't create any new instances of a linked list node.

// --------------------- ACTUAL CODE BELOW

#include <iostream>
using namespace std;

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    // Using a four pointer approach, groups all elements in odd places in the given list 
    // followed by the elements in even places with O(1) space and O(n) time complexity.
    ListNode* CreateOddEvenList(ListNode* head) {
        // Check if the provided linked list is empty and return if yes
        if (head == nullptr) {
            return head;
        }
        
        ListNode *odd_ptr, *even_ptr, *even_head;
        
        // Declare head of even list; head of odd list is head
        even_head = head->next;
        // Declare odd and even pointers
        odd_ptr = head;
        even_ptr = even_head;
        
        // Group elements at odd locations in linked list together; do the same for elements at even locations
        while ((odd_ptr->next != nullptr) && (even_ptr->next != nullptr)) {
            odd_ptr->next = even_ptr->next;
            odd_ptr = odd_ptr->next;
            
            even_ptr->next = odd_ptr->next;
            even_ptr = even_ptr->next;
        }
        
        // Append even list to the end of odd list
        odd_ptr->next = even_head;
        
        // Return the completed odd even linked list
        return head;
    }
};
/*
 * Given the head of a linked list and a value x, partition it 
 * such that all nodes less than x come before nodes greater than or equal to x.
 * 
 * You should preserve the original relative order of the nodes in each of the two partitions
 * 
 * Example 1:
 * Input: head = [1,4,3,2,5,2], x = 3
 * Output: [1,2,2,4,3,5]
 * 
 * Example 2:
 * Input: head = [2,1], x = 2
 * Output: [1,2]
 * 
 * Constraints:
 * > The number of nodes in the list is in the range [0, 200].
 * > -100 <= Node.val <= 100
 * > -200 <= x <= 200
 */

// THOUGHTS
// This implementation was very quickly done since I already coded this solution in Python3. 
// It was good practice with pointers though!
//
// I also made a silly mistake where I set less->next = great_equal 
// rather than less->next = great_equal_head->next, so there was an 
// extra 0 in my returned nodelist before I resolved that.
//
// I also got to allocate memory using the new keyword, 
// though I am confused as to whether or not I'm supposed to deallocate it?

// ------------- ATTEMPT 1

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
    // Partitions a nodelist such that all of the nodes with values less than x 
    // come before all the nodes with values greater than or equal to x
    //
    // Has O(n) time complexity, where n is the number of nodes, 
    // since the loop only goes through each node in the nodelist once. 
    // 
    // O(1) space complexity because I'm only using 5 variables to store important locations in each list.
    ListNode* partition(ListNode* head, int x) {
        if (head == nullptr) {
            return head;
        }
        
        ListNode *ptr = head;
        ListNode *less_head = new ListNode();
        ListNode *less = less_head;
        ListNode *great_equal_head = new ListNode();
        ListNode *great_equal = great_equal_head;
        
        while (ptr != nullptr) {
            if (ptr->val < x) {
                less->next = ptr;
                less = ptr;
            }
            else {
                great_equal->next = ptr;
                great_equal = ptr;
            }
            
            ptr = ptr->next;
        }
        
        less->next = great_equal_head->next;
        great_equal->next = nullptr;
        
        return less_head->next;
    }
};
/* 

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000



*/


#include <stdio.h>
#include <stdlib.h>

/**
 * Definition for singly-linked list.
*/
struct ListNode {
    int val;
    struct ListNode *next;
};
 
struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    int count = 0;
    struct ListNode* temp = head;
    while (temp != NULL)
    {
        count++;
        temp = temp->next;
    }
    int i = count - n;
    int j = 0;
    temp = head;
    if (n != count)
    {
        while(j < i-1)
    {
        temp = temp->next;
        j++;
    }
    }
    else
    {
        head = head->next;
        return head;
    }
    
    if (temp->next == NULL)
    {
        head = NULL;
    }
    else if (temp->next->next == NULL)
    {
        temp->next = NULL;
    }
    
    else
    {
        temp->next = temp->next->next;
    }
    return head;
}
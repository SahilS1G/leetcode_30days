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

struct ListNode {
     int val;
     struct ListNode *next;
};

int traversal(struct ListNode* head)
{
    struct ListNode* temp;
    temp = head;
    int count = 0;
    
    while (temp != NULL)
    {
        count++;
        temp = temp->next;
    }
    return count;
    
}



struct ListNode* reverseKGroup(struct ListNode* head, int k){  
        
        int number_of_nodes = traversal(head);
        int n;
        int count = 0;
        while(n>0)
        {
            n = number_of_nodes - k;
            count++;
        }

        for (int i; i < k/2;i++)
        {
            
        }
}

int main()
{

    return 0;
}

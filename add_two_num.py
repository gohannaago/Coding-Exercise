""" 
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

https://leetcode.com/problems/add-two-numbers/
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        l3 = ListNode() #initialize dummyhead 0
        l3_tail = l3
        carry = 0
        
        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0) #pass excpections where lengths of the lists are different
            sum3 = val1 + val2 + carry
            carry = sum3 // 10
            val3 = sum3 % 10
            
            l3_tail.next = ListNode(val3) #connect the nodes rather than assigning a single value
            l3_tail = l3_tail.next
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        
        return l3.next

solution = Solution()
l1 = ListNode()

solution.addTwoNumbers(l1, l2)

### Delete Node in a Linked List

#### Example
* Input: head = [4,5,1,9], node = 5
* Output: [4,1,9]
* Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 只给了链表节点
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val=node.next.val # 改变当前node值为下一个node
        node.next=node.next.next # 跳过node.next

# 只给了head和要剔除节点的值val
class Solution:
    def deleteNode(self, head, val):
        dummy = ListNode(-1) # 新建一个伪头部，防止要删除第一个节点
        dummy.next = head
        pre = dummy # 记录一个前序节点
        while pre.next: # 如果前序节点后非空
            if pre.next.val == val: # 判断前序节点的后一个节点，即当前节点的值是否是需要删除的值
                pre.next = pre.next.next # 如果满足，则跳过当前节点
            pre = pre.next # 否则前序节点指针后移一位
        return dummy.next # 返回伪头部后面的链表即可

```
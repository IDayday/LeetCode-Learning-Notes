### Reverse Linked List

#### Example 
* Input: head = [1,2,3,4,5]
* Output: [5,4,3,2,1]

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, curr = None, head # 新增一个None节点作为伪头节点，记录当前节点curr
        while curr: # 如果当前节点非空
            tmp = curr.next # 保存当前节点后的链表（指针指向头节点）
            curr.next = pre # 当前节点连接前一个节点
            pre = curr # pre指针指向当前节点
            curr = tmp # curr指针指向保存的头节点
        return pre # 如果curr为空，则其前一个节点就是可返回的头节点

```
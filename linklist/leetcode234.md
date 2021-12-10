### Palindrome Linked List

#### Example

<div align=center>
<img src="pal1linked-list.jpg" width="450" height="65" />
</div>

* Input: head = [1,2,2,1]
* Output: true
_
* Input: head = [1,2]
* Output: false

```python

# 这个方法由于存在遍历存储节点，所以空间复杂度是O(n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, curr = None, head
        while curr:
            tmp = curr.next
            curr.next = pre
            pre = curr
            curr = tmp
        return pre
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        A = [head]
        n = 0
        while head and head.next:
            A.append(head.next)
            n += 1
        pre_mid_node = A[n//2 - 1] 
        mid_node = pre_mid_node.next
        pre_mid_node.next = Node
        re_mid_node = self.reverseList(mid_node)
        return True if re_mid_node == head  else False # 链表直接用 == 是没法判断相等的


# 通过双指针法找到中间位置，可以保证空间复杂度为O(1)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # 反向后半个片段
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        # 进行反向后的片段和前半个片段的比较
        # 链表直接用 == 是没法判断相等的
        while node: 
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True
```
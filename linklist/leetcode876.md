### 876 Middle of the Linked List

#### Example

* Input: head = [1,2,3,4,5]
* Output: [3,4,5]
* Explanation: The middle node of the list is **node** 3.

* Input: head = [1,2,3,4,5,6]
* Output: [4,5,6]
* Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.


```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 用数组存储
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = [head]
        curr = head
        n = 0
        while curr:
            l.append(curr)
            curr = head.next
            head = curr
            n += 1
        return l[(n//2) + 1]
## 简版
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        A = [head]
        while A[-1].next:
            A.append(A[-1].next)
        return A[len(A)//2]


# 单指针两次遍历
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n, curr = 0, head
        while curr:
            n += 1
            curr = curr.next
        
        m, cur = 0, head
        while m < n//2:
            m += 1
            cur = cur.next
        return cur

# 双指针
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head # 快慢两个指针
        while fast and fast.next: # 要求当前节点和下一节点都存在，如果仅当前节点存在，head为odd时有误。如果仅下一节点存在，head为even时有误。
            fast = fast.next.next # 快的走两步
            slow = slow.next # 慢的走一步
        return slow

        

```
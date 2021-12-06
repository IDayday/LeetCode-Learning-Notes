### Remove Duplicates from Sorted List

#### Example

* Input: head = [1,1,2]
* Output: [1,2]

* Input: head = [1,1,2,3,3]
* Output: [1,2,3]

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 该方法可行，但是超时了，通过对比当前节点和下一节点的val，如果相同则跳过下一节点。
# 麻烦的地方在于当末尾两个节点值相同时，需要单独判断，增加了耗时。
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        latter = head.next
        while curr and latter:
            if latter.next:
                if curr.val == latter.val:
                    curr.next = latter.next
                    curr = latter.next
                    latter = curr.next
                else:
                    curr = latter
                    latter = curr.next
            else:
                if curr.val == latter.val:
                    curr.next = None
                else:
                    continue
        
        return head

# 改进后
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        if not curr or not curr.next:
            return head
        else:
            latter = head.next
        while curr and latter:
            if curr.val == latter.val:
                curr.next = latter.next
                latter = latter.next
            else:
                curr = latter
                latter = curr.next
        return head


# 嵌套迭代法，不使用指针
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: # 可以判断空，单节点。如果当前节点已是末尾节点，也可直接返回。
            return head
        h = self.deleteDuplicates(head.next) # 迭代使用函数，找到最邻近的下一个不同节点，若已到末尾，会返回末尾节点给 h
        head.next = h if head.val != h.val else h.next # 这里处理末尾两个相同节点，由于h已是末尾节点，所以h.next为None
        return head

# 这种方法恰好是我想表达的，但是没能简化过程，设计得繁琐了
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head # 记录头节点
        while node and node.next: # 判断当前节点和临接节点存在
            if node.val == node.next.val: # 如果值相同
                node.next = node.next.next # 则跳过临接节点，这里如果遇到末尾相同的两个节点，node.next.next恰好为None，也是能处理的
            else:
                node = node.next # 如果值不同，则指针指向下一位
        return head

# 引入字典统计的方法
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dic = {}
        node = head
        while node:
            dic[node.val] = dic.get(node.val, default=0) + 1 #  get() 函数返回指定键的值，default -- 如果指定键的值不存在时，返回该默认值。统计各个不同节点值，并记录出现次数形成键值对。
            node = node.next
        node = head
        while node:
            tmp = node
            for _ in range(dic[node.val]): # 要求是有序的链表，无序的没法处理，Discussion中有人人为这种方法可以处理无序链表是错的
                tmp = tmp.next # 指针指向最邻近的不同节点，因为统计过相同节点数，在range中恰好循环对应次数，能让指针跳过所有相同的值
            node.next = tmp # 跳跃连接
            node = node.next # 更新当前node
        return head


```
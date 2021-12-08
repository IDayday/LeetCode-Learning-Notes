### Swap Nodes in Pairs

#### Example

<div align=center>
<img src="swap_ex1.jpg" width="450" height="250" />
</div>

* Input: head = [1,2,3,4]
* Output: [2,1,4,3]

* Input: head = []
* Output: []

* Input: head = [1]
* Output: [1]

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head # 针对空集合和单元素集合
        dummy = ListNode(0) # 用一个虚拟的头节点
        dummy.next = head
        cur = dummy # 当前指针定位到虚拟头
        
        while cur.next and cur.next.next: # 当前指针下一个和下下一个节点存在时才交换位置
            # 这里重标记的原因是：在后面的交换过程中，关键一步：后一个节点的next指向前一个节点，
            # 这一步如果没有重标记，那么就丢失了后一个节点往后所有的链，而重标记，也就是备份一次就可再找回来。 
            first = cur.next # 重标记下一个节点
            sec = cur.next.next # 重标记下下一个节点
            cur.next = sec # 指针的下一节点是sec，此时sec后面的链还没有丢失
            first.next = sec.next # 备份的first接上sec后面的链
            sec.next = first # 这时候才放心将sec后面接first
            cur = cur.next.next # 指针后移两位
        return dummy.next  # 因为是虚拟头，所以返回后面的链


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        new_start = head.next.next # 先标记后移两位的node
        head, head.next = head.next, head # 利用python的交换机制，这一步交换，保持了head作为头，且与next发生了交换
        head.next.next = self.swapPairs(new_start) # 这里传入新标记位，仍以head作为头，所以后面返回head时，输出的是完整链
        # 这里的嵌套可以进一步理解为：每一次调用函数，就是进行一组交换，然后通过
        # head.next.next = self.swapPairs(new_start)
        # 赋值操作保证能接上之前的链，所以最后输出可以倒过来看，
        # 完成最后一组交换，再接上这次调用的函数，赋值给head.next.next，
        # 那么在这一层函数调用中，head的意义已经再往前移了两位。
        # 每次都是接上，然后head前移两位，知道最后回到初始的第一层函数，这里的head就是真正的头了，
        # 所以返回head就是返回完整链。
        return head

```
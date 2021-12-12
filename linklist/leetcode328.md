### Odd Even Linked List

#### Example

<div align=center>
<img src="oddeven-linked-list.jpg" width="350" height="" />
</div>

* Input: head = [1,2,3,4,5]
* Output: [1,3,5,2,4]

<div align=center>
<img src="oddeven2-linked-list.jpg" width="450" height="" />
</div>

* Input: head = [2,1,3,5,6,4,7]
* Output: [2,3,6,7,1,5,4]

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy1 = odd = ListNode(0) # 设置虚拟奇队列头
        dummy2 = even = ListNode(0) # 设置虚拟偶队列头
        while head:
            odd.next = head # 奇队列头接一个
            even.next = head.next # 偶队列接一个
            odd = odd.next # 奇队列指针后移一位
            even = even.next # 偶队列指针后移一位
            head = head.next.next if even else None # 如果偶队列存在，则原始链表指针后移两位，否则置为None
        odd.next = dummy2.next # 奇队列末尾连上偶队列头
        return dummy1.next # 返回奇队列头即可

# 区分奇偶也可以用计数来区分
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d1=odd=ListNode(0)
        d2=even=ListNode(0)
        i=1
        while head:
            if i%2: # 当前指针为奇数位
                odd.next,odd=head,head # 奇队列接一个，指针同步到原始链表指针
            else: # 当前指针为偶数位
                even.next,even=head,head # 偶队列接一个，指针同步到原始链表指针
            head=head.next # 原始链表指针后移一位
            i += 1 # 计数
        odd.next,even.next=d2.next,None # 奇队列末尾连接偶队列头，偶队列这里需要用None断开
        # 具体来说，如果是[1,2]则没关系，
        # 如果是[1,2,3]，那么会odd = head，接就是当前odd在3位置上，而even还在2位置上，2本来连着3，如果不断开，那么会陷入1->3->2->3->2->3->...的死循环
        return d1.next
```
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None
# 头插法
def create_linklist(l):
    # 找出当前的头
    head = ListNode(l[0])
    # 遍历 l 的值，将后面的element都以头插法形式放在头部
    for element in l[1:]:
        # 生成一个新节点
        node = ListNode(element)
        # 连接上之前的节点
        node.next = head
        # 重新定向头部
        head = node
    # 最后返回头部即可返回完整链表
    return head

# 尾插法
def create_linklist_tail(l):
    head = ListNode(l[0])
    tail = head
    for element in l[1:]:
        node = ListNode(element)
        tail.next = node
        tail = node
    return head



def print_linklist(lk):
    while lk:
        print(lk.val, end="->")
        lk = lk.next


# lk = create_linklist_tail([1,2,3,4])
# index = 2
# node = ListNode(5)
# print(lk.val)
# print(lk.next.val)

# 链表插入
def inter_after(lk ,index, node):
    dummy = lk
    for i in range(index-1):
        catnode = dummy.next
        head = dummy.next
        dummy = head
    node.next = catnode.next
    catnode.next = node
    return lk,dummy

# new_lk, dummy = inter_after(lk, index, node)
# print_linklist(new_lk)
# output: 1->2->5->3->4->
# print_linklist(dummy)
# output: 2->5->3->4->


class Solution:
    def reverseList(self, head):
        pre, curr = None, head # 新增一个None节点作为伪头节点，记录当前节点curr
        while curr: # 如果当前节点非空
            tmp = curr.next # 保存当前节点后的链表（指针指向头节点）
            curr.next = pre # 当前节点连接前一个节点
            pre = curr # pre指针指向当前节点
            curr = tmp # curr指针指向保存的头节点
        return pre # 如果curr为空，则其前一个节点就是可返回的头节点
    def addTwoNumbers(self, l1, l2):
        re_l1 = self.reverseList(l1)
        re_l2 = self.reverseList(l2)
        head = None
        carry = 0
        while re_l1 or re_l2 or carry:
            v1 = re_l1.val if re_l1 else 0
            v2 = re_l2.val if re_l2 else 0
            carry, val = divmod(v1 + v2 + carry, 10)
            head = ListNode(val, head)
            re_l1 = re_l1.next if re_l1 else None
            re_l2 = re_l2.next if re_l2 else None
        return head

S = Solution()
lk_1 = create_linklist_tail([7,2,4,3])
lk_2 = create_linklist_tail([5,6,4])
add_sum = S.addTwoNumbers(lk_1,lk_2)
print_linklist(add_sum)

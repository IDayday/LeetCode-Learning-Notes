from typing import List


class ListNode:
    def __init__(self, val, next=None):
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


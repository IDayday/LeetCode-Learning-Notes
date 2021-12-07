### Merge two sorted lists

#### Example
* Input: 1->2->4, 1->3->4
* Output: 1->1->2->3->4->4

ListNode定义的属性包含val和next

由于要不断比较list1和list2中的元素的大小，所以需要有一个记录点来记录当前比较后插入的位置（curr），另外输出要求是完整的list，所以需要另一个保持不变的副本来记录（dummy）

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy = ListNode(0)

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            
            curr = curr.next
        curr.next = list1 or list2
        return dummy.next
```

### 补充知识
* 链表是由一系列节点组成的元素集合。
* 双链表的每个节点有两个指针，一个指向前一个节点，一个指向后一个节点。（其插入和删除与单链表类似，多一倍操作）
* 顺序表（列表/数组）与链表————操作的时间复杂度分析
    * 按元素查找：都是O(N)，挨个找，找到为止
    * 按下标查找：顺序表O(1)，链表O(N)
    * 在某元素后插入：顺序表O(N)，链表O(1)
    * 删除元素：顺序表O(N)，链表O(1)
* 所以链表的内存分配更加灵活

#### 创建链表
* 头插法
比如已有两个节点组成的链表，新来一个节点，就将头指向新来的节点，并连接原来的头节点，从而实现三个节点链表的生成。
* 尾插法
不光要知道头在哪，还要知道尾在哪，来一个新的节点，放在尾端。

```python
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

# 显示链表结构
def print_linklist(lk):
    while lk:
        print(lk.val, end="->")
        lk = lk.next

# 尾插法
def create_linklist_tail(l):
    head = ListNode(l[0])
    tail = head
    for element in l[1:]:
        node = ListNode(element)
        tail.next = node
        tail = node
    return head

```

#### 链表的插入和删除
```python

# 将 5 插入 1->2->3->4 中 2 的后面
def inter_after(lk ,index, node):
    dummy = lk
    for i in range(index-1):
        catnode = dummy.next
        head = dummy.next
        dummy = head
    node.next = catnode.next
    catnode.next = node
    return lk,dummy

```




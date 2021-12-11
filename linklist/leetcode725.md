### Split Linked List in Parts

#### Example

* Input: head = [1,2,3], k = 5
* Output: [[1],[2],[3],[],[]]
* Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].
_
* Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
* Output: [[1,2,3,4],[5,6,7],[8,9,10]]
* Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 这题一般可以分为三个步骤
# 1.求得总链长
# 2.计算每段长度
# 3.划分出来
class Solution(object):
    def splitListToParts(self, root, k):
        # 计算链长
        curr, length = root, 0
        while curr:
            curr, length = curr.next, length + 1
        # 计算每段长度
        chunk_size, longer_chunks = length // k, length % k 
        # chunk_size：每段平均长度
        # longer_chunks：余数，决定第一段长度
        res = [chunk_size + 1] * longer_chunks + [chunk_size] * (k - longer_chunks)
        # 举例链长为10，k为3.
        # chunk_size = 3
        # longer_chunks = 1
        # [chunk_size + 1] * longer_chunks = [4]
        # [chunk_size] * (k - longer_chunks) = [3,3]
        # 相加得 res = [4,3,3]
        # Split up the list
        prev, curr = None, root
        for index, num in enumerate(res):
            if prev: # 每进入下一个片段时，prev表示上一个片段末尾节点，所以next设置为None
                prev.next = None
            res[index] = curr # curr记录的当前片段的起始节点
            # 这里res = [4,3,3]
            # 替换为对应片段的起始节点，最终作为输出
            for i in range(num):
                prev, curr = curr, curr.next
        return res
```
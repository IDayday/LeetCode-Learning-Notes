### Implement Queue using Stacks

### 补充知识

#### 栈
* 栈（stack）是一个数据集合，可以理解为只能在一端进行插入或者删除的列表。
* 栈的特点：后进先出 LIFO(last-in, first-out)
* 栈的概念：栈顶，栈底
* 栈的基本操作：
    * 进栈（压栈）：push
    * 出栈：pop
    * 取栈顶：gettop（只获取栈顶信息，不取走）

_
* 一般用列表的结构即可实现栈结构
    * 进栈：list.append
    * 出栈：list.pop
    * 取栈顶：list[-1]
_
* 栈的应用之一———括号匹配问题
()[]{} : 匹配
{[([()])]} : 匹配
[]) : 不匹配

#### 队列
* 队列（queue）是一个数据集合，仅允许在列表的一端进行插入，另一端进行删除
* 进行插入的一端叫队尾（rear），插入动作称为进队或者入队。
* 进行删除的一端叫对头（front），删除的动作称为出队。
* 队列的性质：先进先出FIFO（first-in，first-out）


#### Example

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

**Implement the MyQueue class:**

* void push(int x) Pushes element x to the back of the queue.
* int pop() Removes the element from the front of the queue and returns it.
* int peek() Returns the element at the front of the queue.
* boolean empty() Returns true if the queue is empty, false otherwise.

**Notes:**

* You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
* Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

**Input**
* ["MyQueue", "push", "push", "peek", "pop", "empty"]
* [ [], [1], [2], [], [], [] ]

**Output**
* [null, null, null, 1, 1, false]

**Explanation**
>MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false

```python
# 本题就体现了用列表实现栈，然后利用栈实现队列
class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x): # 进队，从尾部添加
        self.s1.append(x)

    def pop(self):
        self.peek() # 获得反向的s2
        return self.s2.pop() # s2的尾就是s1的头，即实现了队列的出队

    def peek(self): # 利用s2反向存储s1的元素，这样s2[-1]就是s1的头
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]        

    def empty(self): # 判断队列是否为空
        return not self.s1 and not self.s2 


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```

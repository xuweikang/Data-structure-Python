# 线性表的实现


class NodeList:  # 链表元素
    def __init__(self, ele, next_=None):
        self.ele = ele
        self.next = next_


class LListSingle:  # 单向链表的实现
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def length(self):
        if self.is_empty():
            return 0
        current = self._head
        count = 1

        while current is not None:
            count += 1
            current = current.next

        return count

    def add(self, ele):
        q = NodeList(ele, self._head)
        self._head = q

    def insert(self, elem, index):
        if self.is_empty() or index < 0 or index > self.length():
            print('error is throw')
        if index == 0:  # 头部插入
            q = NodeList(elem, self._head)
            self._head = q
        else:
            current = self._head
            ele = NodeList(elem)
            while index:
                index -= 1
                pre, current = current, current.next
            pre.next = ele
            ele.next = current

    def findByIndex(self, index):
        if self.is_empty():
            print('error is throw')
            return
        if index < 0 or index > self.length():
            print('not fond')
            return
        if index == 0:
            return self._head.ele
        current = self._head
        while index:
            index = index - 1
            pre, current = current, current.next
        return current.ele

    def delete(self, ele):
        pre, found, curr = None, False, self._head
        while not found and (curr is not None):
            if curr.ele == ele:
                found = True
            else:
                pre, curr = curr, curr.next
        if found == False:
            print("not found {0}".format(ele))
        elif curr == self._head:  # 删除的是头元素
            self._head = self._head.next
        else:
            pre.next = curr.next

    def print(self):
        if self.is_empty():
            print('暂无list')
        else:
            current = self._head
            pri = []
            while current != None:
                pri.append(current.ele)
                current = current.next
            print(pri)


list = LListSingle()
list.add(0)
list.add(1)
list.add(2)
list.insert(3, 0)
list.insert(4, 1)
list.insert(10086, 3)
list.print()
list.delete(10086)
list.print()
print(list.findByIndex(3))

print('--------------分割线--------------')


class LListSingleLoop:  # 循环单链表的实现
    def __init__(self):
        self._rear = None  # 指向尾节点

    def is_empty(self):
        return self._rear is None

    def add(self, ele):
        q = NodeList(ele)
        if self._rear is None:  # 如果是空链表，则建立一个节点的环
            q.next = q
            self._rear = q
        else:
            q.next = self._rear.next
            self._rear.next = q

    def append(self, ele):
        self.add(ele)
        self._rear = self._rear.next

    def pop(self):
        if self._rear is None:
            print('the list is none')
        p = self._rear.next
        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next
        return p.ele

    def print(self):
        if self.is_empty():
            print('暂无list')
        else:
            current = self._rear
            pri = []
            count = 0
            while True:
                if current is self._rear and count > 0:
                    break
                pri.append(current.ele)
                current = current.next
                count += 1
            print(pri)


listLoop = LListSingleLoop()
listLoop.add('a')
listLoop.add('b')
listLoop.add('c')
listLoop.append('d')
print('被pop的元素是' + listLoop.pop())
listLoop.print()

print('--------------分割线--------------')


class NodeListDouble(NodeList):  # 双链表节点
    def __init__(self, ele, prev=None, next_=None):
        NodeList.__init__(self, ele, next_)
        self.prev = prev


class LListDouble(LListSingle):  # 双链表的实现
    def __init__(self):
        LListSingle.__init__(self)
        self._head = None

    def is_empty(self):
        return LListSingle.is_empty(self)

    def length(self):
        return LListSingle.length(self)

    def add(self, ele):
        q = NodeListDouble(ele, None, self._head)
        self._head = q

    def insert(self, elem, index):
        if self.is_empty() or index < 0 or index > self.length():
            print('error is throw')
        if index == 0:  # 头部插入
            q = NodeListDouble(elem, None, self._head)
            self._head = q
        else:
            current = self._head
            ele = NodeListDouble(elem)
            while index:
                index -= 1
                pre, current = current, current.next
            ele.prev = pre
            ele.next = current
            pre.next = ele
            current.pre = ele

    def findByIndex(self, index):
        if self.is_empty():
            print('error is throw')
            return
        if index < 0 or index > self.length():
            print('not fond')
            return
        if index == 0:
            return self._head.ele
        current = self._head
        while index:
            index = index - 1
            pre, current = current, current.next
        return current.ele

    def print(self):
        if self.is_empty():
            print('暂无list')
        else:
            current = self._head
            pri = []
            while current != None:
                pri.append(current.ele)
                current = current.next
            print(pri)


listDouble = LListDouble()
listDouble.add('a')
listDouble.add('b')
listDouble.add('c')
listDouble.insert('d', 2)
listDouble.print()


print('--------------分割线--------------')


class LListDoubleLoop(LListDouble):  # 循环双链表的实现
    def __init__(self):
        LListDouble.__init__(self)

    def is_empty(self):
        return LListDouble.is_empty(self)

    def length(self):
        return LListDouble.length(self)

    def add(self, ele):
        q = NodeListDouble(ele)
        if self.is_empty():  # 空表建立一个自闭环
            q.next = q
            q.prev = q
            self._head = q
        else:
            q.next = self._head
            q.prev = self._head.prev
            self._head.prev.next = q
            self._head.prev = q
            self._head = q

    def append(self, ele):
        if self.is_empty():
            self.add(ele)
            return
        elem = NodeListDouble(ele)
        elem.prev = self._head.prev
        elem.next = self._head
        self._head.prev.next = elem
        self._head.prev = elem

    def pop(self):  # 删除最后一个元素
        if self.is_empty():
            print('list is None')
            return
        lastNode = self._head.prev
        lastNode.prev.next = lastNode.next
        self._head.prev = lastNode.prev
        return lastNode.ele

    def shift(self):  # 删除第一个元素
        if self.is_empty():
            print('list is None')
            return
        nodeHead = self._head.ele
        self._head.next.prev = self._head.prev
        self._head.prev.next = self._head.next
        self._head = self._head.next
        return nodeHead

    def print(self):
        if self.is_empty():
            print('暂无list')
        else:
            current = self._head
            pri = []
            pri.append(current.ele)
            current = current.next
            while 1:
                if current == self._head:
                    break
                pri.append(current.ele)
                current = current.next
            print(pri)


listDoubleLoop = LListDoubleLoop()
listDoubleLoop.append('x')
listDoubleLoop.append('w')
listDoubleLoop.append('k')
listDoubleLoop.append('i')
print(listDoubleLoop.pop())
listDoubleLoop.print()
listDoubleLoop.add('j')
print(listDoubleLoop.shift())
listDoubleLoop.print()

# 线性表的实现
class NodeList:  # 链表元素
    def __init__(self, ele, next_=None):
        self.ele = ele
        self.next = next_


class LListSingle: # 单向链表的实现
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
        if index == 0:   # 头部插入
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
            return self._head.elem
        while index:
            index = index -1


    def delete(self):


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
list.print()
# list.insert(3, 0)
# list.print()
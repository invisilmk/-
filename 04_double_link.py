

class Node(object):
    def __init__(self,item):
        self.elem = item
        self.next = None
        self.pre = None
class SingleLinkList(object):

    def __init__(self,node=None):
        self._head = node

    def is_empty(self):  #对象方法
        return self._head == None

    def length(self):
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self._head
        while cur != None:
            print(cur.elem)
            cur = cur.next

    def add(self,item):
        node = Node(item)

        node.next = self._head
        self._head = node
        node.next.pre = node


    def append(self,item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.pre = cur










    def insert(self,pos,item):
        if pos<=0:
            self.add(item)
        elif pos>(self.length()-1):
            self.append(item)
        else:
            pre = self._head
            count = 0
            while count<=pos:
                count += 1
                pre = pre.next
            node = Node(item)
            node.next = pre.next
            pre.next = node

            # node = Node(item)
            # while pos != 0:
            #     cur = cur.next
            #     pos -= 1
            #
            # node.next = cur.next
            # cur.next = node

    def remove(self,item):
        cur = self._head
        pre = None
        while cur != None:
            if cur.elem == item:
                if cur == self._head:
                    self._head == cur.next
                else:
                #cur = cur.next.next
                    pre.next = cur.next
                break
                #pre = cur.next
            else:
                pre = cur
                cur = cur.next

    def search(self,item):
        cur = self._head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False



    pass
if __name__ == '__main__':
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())
    ll.append(1)
    print(ll.length())
    ll.travel()
node = Node(100)
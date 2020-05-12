class Node(object):
    def __init__(self,item):
        self.elem = item
        self.lchild= None
        self.rchild= None

class Tree(object):
    def __init__(self):
        self.root = None

    def add(self,item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = []
        queue.append(self.root)
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
            else:
                queue.append(cur_node.rchild)
    def preorder(self,node):
        if node is None:
            return
        print(node.elem)
        self.preorder(node.lchild)
        self.preorder(node.rchild)
    def preorder(self,node):
        if node is None:
            return

        self.preorder(node.lchild)
        print(node.elem)
        self.preorder(node.rchild)
if __name__ == '__main__':
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.preorder(tree.root)
    print(' ')




#完全二叉树，增添与遍历
class Node():
    def __init__(self,val):
        self.item=val
        self.lbranch=None
        self.rbranch=None
#新建一个二叉树
class BinaryTree():
    def __init__(self):
        self.root=None
    def add(self,val):
        node=Node(val)
        if self.root is None:
            self.root=node
            return
        queue_tree=[self.root]
        while queue_tree:
            cur_node=queue_tree.pop(0)
            if cur_node.lbranch is None:
                cur_node.lbranch=node
                return
            else:
                queue_tree.append(cur_node.lbranch)
            if cur_node.rbranch is None:
                cur_node.rbranch=node
                return
            else:
                queue_tree.append(cur_node.rbranch)
#广度遍历
    def spared_tree_view(self):
        if self.root is None:
            return
        queue_tree = [self.root]
        while queue_tree:
            cur_node=queue_tree.pop(0)
            print(cur_node.item,end=" ")
            if cur_node.lbranch is not None:
                queue_tree.append(cur_node.lbranch)
            if cur_node.rbranch is not None:
                queue_tree.append(cur_node.rbranch)
#先序查找
    def left_sortree(self,node):
        if node is None:
            return
        print(node.item,end=" ")
        self.left_sortree(node.lbranch)
        self.left_sortree(node.rbranch)
#中序查找
    def middle_sortree(self,node):
        if node is None:
            return
        self.middle_sortree(node.lbranch)
        print(node.item,end=" ")
        self.middle_sortree(node.rbranch)
#后序查找
    def right_sortree(self,node):
        if node is None:
            return
        self.right_sortree(node.lbranch)
        self.right_sortree(node.rbranch)
        print(node.item,end=" ")


if __name__=='__main__':
    b_Tree=BinaryTree()
    b_Tree.add(0)
    b_Tree.add(1)
    b_Tree.add(2)
    b_Tree.add(3)
    b_Tree.add(4)
    b_Tree.add(5)
    b_Tree.add(6)
    b_Tree.add(7)
    b_Tree.add(8)
    b_Tree.add(9)
    b_Tree.spared_tree_view()
    print()
    b_Tree.left_sortree(b_Tree.root)
    print()
    b_Tree.middle_sortree(b_Tree.root)
    print()
    b_Tree.right_sortree(b_Tree.root)





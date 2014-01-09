class My_Tree(object):
    def __init__(self):
        self.root = None

    def r_make_binary_search(self, l):
        if not l:
            return
        pivot = len(l)/2
        node = My_Node(l[pivot])
        node.left = self.r_make_binary_search(l[:pivot])
        node.right = self.r_make_binary_search(l[pivot+1:])
        return node

    def make_binary_search(self, l):
        self.root = self.r_make_binary_search(l)

    def r_print_tree(self, node):
        if not node:
            return
        else:
            print node.data
            self.r_print_tree(node.left)
            self.r_print_tree(node.right)

    def print_tree(self):
        self.r_print_tree(self.root)

class My_Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

l = range(1,10)
my_tree = My_Tree()
my_tree.make_binary_search(l)
my_tree.print_tree()
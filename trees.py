class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def tree_height(tree):
    if not tree or not tree.data:
        return 0
    else:
        # l = tree_height(tree.left)
        # r = tree_height(tree.right)

        # return max(l,r)+1
        return max(tree_height(tree.left), tree_height(tree.right))+1



def main():
    node1 = Node(5)
    node2 = Node(2)
    node3 = Node(1)
    node4 = Node(7)
    node5 = Node(10)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node4.left = node5

    print tree_height(node1)

main()
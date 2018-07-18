class Node:
    def __init__(btree,key):
        btree.left=None
        btree.right=None
        btree.val=key
def printPreorder(root):
    if root:
        print(root.val)
        printPreorder(root.left)
        printPreorder(root.right)
def compareValue(root1,root2):
        if root1 is None and root2 is None:
            return True
        if root1 is not None and root2 is not None:
            return root1.val==root2.val and compareValue(root1.left,root2.left) and compareValue(root1.right,root2.right)
        return False
root1=Node(50)
root1.left=Node(20)
root1.right=Node(60)
root1.left.left=Node(10)
root1.left.right=Node(30)

root2=Node(50)
root2.left=Node(20)
root2.right=Node(60)
root2.left.left=Node(10)
root2.left.right=Node(30)

print("Tree 1 Pre-order traversal:")
printPreorder(root1)

print("Tree 2 Pre-order traversal:")
printPreorder(root2)

if compareValue(root1,root2):
    print("Trees are identical")
else:
    print("Trees are not identical")

        

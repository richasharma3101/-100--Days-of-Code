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
def maxHeight(root):
    if root is None:
        return 0
    else:
        lHeight=maxHeight(root.left)
        rHeight=maxHeight(root.right)
        if lHeight>rHeight:
            return lHeight+1
        else:
            return rHeight+1
root=Node(50)
root.left=Node(20)
root.right=Node(60)
root.left.left=Node(10)
root.left.right=Node(30)

print("Tree Pre-order traversal:")
printPreorder(root)
print("Height of tree is %d ",(maxHeight(root)))


        

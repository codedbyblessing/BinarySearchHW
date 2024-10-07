from BinarySearchTreeMap import BinarySearchTreeMap

def create_chain_bst(n):
    bst = BinarySearchTreeMap()
    flattened_tree = bst
    pos = 1
    while pos <= n:
        flattened_tree.insert(pos,pos)
        pos +=1
    return flattened_tree

def create_complete_bst(n):
    bst = BinarySearchTreeMap()
    add_items(bst, 1, n)
    return bst

def add_items(bst, low, high):
    if low == high:
        bst.insert(low, low)
    else:
        mid_root = (low + high) // 2
        bst.insert(mid_root, mid_root)
        add_items(bst, low, mid_root - 1)
        add_items(bst, mid_root + 1, high)







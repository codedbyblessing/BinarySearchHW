from BinarySearchTreeMap import BinarySearchTreeMap

def restore_bst(prefix_lst):
    if len(prefix_lst)== 0:
        return BinarySearchTreeMap()
    if len(prefix_lst) == 1:
        bst = BinarySearchTreeMap()
        bst.insert(prefix_lst[0], prefix_lst[0])

        return bst
    maxi = max(prefix_lst)+1
    mini = min(prefix_lst)-1
    starting_pos = 0

    def helper_func(prefix_lst, starting_pos, maxi, mini):
        if starting_pos >= len(prefix_lst):
            return None, starting_pos
        if prefix_lst[starting_pos] > maxi or prefix_lst[starting_pos] < mini:
            return None, starting_pos

        item = BinarySearchTreeMap.Item(prefix_lst[starting_pos], prefix_lst[starting_pos])
        curr = BinarySearchTreeMap.Node(item)
        left = helper_func(prefix_lst, starting_pos+1, prefix_lst[starting_pos], mini)
        right = helper_func(prefix_lst, left[1], maxi, prefix_lst[starting_pos])
        curr.right = right[0]
        curr.left = left[0]

        if right[0] != None:
            right[0].parent = curr
        if left[0] != None:
            left[0].parent = curr
        return curr, right[1]


    bst = BinarySearchTreeMap()
    nodes = helper_func(prefix_lst, starting_pos, maxi, mini)
    bst.n = len(prefix_lst)
    bst.root = nodes[0]
    return bst



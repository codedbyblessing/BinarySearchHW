def find_min_abs_difference(bst):
    def helper_function(node):
        if node is None:
            return float('inf'), float('-inf'), None

        min_left, max_left, left_leaf = helper_function(node.left)
        min_right, max_right, right_leaf = helper_function(node.right)

        minimum = min(node.item.key if min_left == float('inf') else min_left, node.item.key)
        maximum = max(node.item.key if max_right == float('-inf') else max_right, node.item.key)

        if left_leaf is not None and right_leaf is not None:
            node_diff = min(left_leaf, right_leaf, node.item.key - max_left, min_right - node.item.key)
        elif left_leaf is not None:
            node_diff = min(left_leaf, node.item.key - max_left)
        elif right_leaf is not None:
            node_diff = min(right_leaf, min_right - node.item.key)
        else:
            node_diff = float('inf')

        return minimum, maximum, node_diff

    if not bst.root or (not bst.root.left and not bst.root.right):
        raise ValueError("Tree does not have enough nodes to search through")

    return helper_function(bst.root)[2]

    return result

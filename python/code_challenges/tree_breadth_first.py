def breadth_first(tree):
    # create a queue to hold previously visited nodes
    queue = []
    # return value list
    values = []
    if tree.root is None:
        return values
    if tree.root:
        queue.insert(0, tree.root)
    # while queue is not empty traverse tree
    while queue:
        # pop node from queue list and append that to values list
        node = queue.pop()
        values.append(node.value)
        if node.left:
            # insert this node to queue and loop back around
            queue.insert(0, node.left)
        if node.right:
            queue.insert(0, node.right)
    return values

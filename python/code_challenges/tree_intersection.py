from data_structures.binary_tree import BinaryTree


def tree_intersection(tree_1, tree_2):
    tree_1_dict = {}
    tree_2_dict = {}

    # if either tree has nonexistent root return None
    if not tree_1.root or not tree_2.root:
        return None

    def make_dict(root, dic):
        """
        keep calling make_dic as long as a left exists
        same for right
        """
        if root.left:
            make_dict(root.left, dic)
        if root.right:
            make_dict(root.right, dic)
        # add values to dictionary as keys with val of None
        dic[root.value] = None

    make_dict(tree_1.root, tree_1_dict)
    make_dict(tree_2.root, tree_2_dict)
    matches = [key for key in tree_1_dict.keys() if key in tree_2_dict.keys()]
    # return [key for key in tree_1_dict.keys() if key in tree_2_dict.keys()]
    return matches if matches != [] else None

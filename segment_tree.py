from math import ceil, log


class SegmentTree:
    @staticmethod
    def get_root_index(array):
        if log(len(array) + 1, 2) == int(log(len(array), 2)):
            index_root = 2
        else:
            index_root = 1
        return index_root

    @staticmethod
    def make_tree(array):
        if log(len(array), 2) != int(
                log(len(array), 2)):
            tree = SegmentTree.prepare_tree((2 ** (ceil(log(len(array), 2)) + 1)) - len(array)) + array
        else:
            tree = SegmentTree.prepare_tree(2 ** int(log(len(array), 2)) - len(array)) + array
        return tree

    @staticmethod
    def prepare_tree(size):
        tree = []
        for i in range(size):
            tree.append(['None', 0])
        return tree

    @staticmethod
    def get_max(tree, array):
        return tree[SegmentTree.get_root_index(array)]

    @staticmethod
    def translate_index(tree, array, index):
        return len(tree) - (len(array) - index)

    @staticmethod
    def build(tree, array):
        last_parent = -1
        for i in range(len(tree) - 1, SegmentTree.get_root_index(array), -1):
            if last_parent != i // 2:
                if type(tree[i]) != int and type(tree[i // 2]):
                    if tree[i][1] >= tree[i - 1][1]:
                        tree[i // 2] = tree[i]
                    else:
                        tree[i // 2] = tree[i - 1]
                last_parent = i // 2
        return tree

    @staticmethod
    def update(tree, array, index, value):
        if type(tree[index]) != int:
            root_index = SegmentTree.get_root_index(array)
            if root_index > index:
                return 0
            if index >= len(tree) - len(array):
                tree[index] = value
                SegmentTree.update(tree, array, index // 2, value)
            else:
                if tree[index * 2][1] >= tree[index * 2 + 1][1]:
                    tree[index] = tree[index * 2]
                else:
                    tree[index] = tree[index * 2 + 1]
                SegmentTree.update(tree, array, index // 2, value)

'''
2. Закодируйте любую строку по алгоритму Хаффмана.
'''

# При разработке использовалось решение со странички https://www.programiz.com/dsa/huffman-coding
from collections import Counter


def Huffman_encode(string: str) -> str:
    sorted_freqs = [(k, v) for k, v in sorted(
        Counter(string).items(), key=lambda item: item[1])]

    tree_nodes = sorted_freqs.copy()

    while len(tree_nodes) > 1:
        (key1, c1) = tree_nodes[0]
        (key2, c2) = tree_nodes[1]
        tree_nodes = tree_nodes[2:]
        node = NodeTree(key1, key2)
        tree_nodes.append((node, c1 + c2))
        tree_nodes = sorted(tree_nodes, key=lambda x: x[1])

    huffmanCode = build_tree(tree_nodes[0][0])
    print('Таблица кодирования:')
    print(' Символ | Huffman код ')
    print('----------------------')
    for (char, frequency) in sorted_freqs:
        print(' %-6r |%12s' % (char, huffmanCode[char]))

    result = ''

    for s in string:
        result += huffmanCode[s]

    return result


class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


def build_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(build_tree(l, True, binString + '0'))
    d.update(build_tree(r, False, binString + '1'))
    return d


s = input('Введите произвольную строку: ')
s_encoded = Huffman_encode(s)
print(f'Закодированная по Хаффману строка: {s_encoded}')

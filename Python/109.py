string = 'AACAGAABAACGB'


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


# budowanie drzewka, jak chcemy po gałązkach iść na lewo to jest 0 jak na prawo to 1
def huffman_tree(node, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_tree(l, binString + '0'))
    d.update(huffman_tree(r, binString + '1'))
    return d


# liczymy wartości występowania danego znaku
freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1
# sortowanko i przypisanie do nowej zmiennej
freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodes = freq
# wyrzucamy dwie najmniejsze wartości ze zbioru liczymy ich sumę dopóki wszystkie elementy nie zostaną przeliczone
while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_tree(nodes[0][0])

print(' Znak | Zakodowana wiadomość ')
print('----------------------')
for (char, frequency) in freq:
    print(' %-4r |%12s' % (char, huffmanCode[char]))

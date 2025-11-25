from queue import Queue
import random

ROOT = "root"
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node)
    
    def height(self, node=None):
        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        if hright > hleft:
            return hright + 1
        return hleft + 1

    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left)
        print(node, end=' ')
        if node.right:
            self.inorder_traversal(node.right)

    def levelorder_traversal(self, node=ROOT):
        if node == ROOT:
            node = self.root
        
        if not node:
            return

        queue = Queue()
        queue.put(node) 

        while not queue.empty(): 
            node = queue.get() 
            print(node, end=" ")
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)
        return None
    
    def isSameTree(self, other_tree):
        """
        Compara esta árvore com outra BinaryTree.
        other_tree deve ser uma instância de BinaryTree.
        """
        return self._isSameTree_recursive(self.root, other_tree.root)

    def _isSameTree_recursive(self, p_node, q_node):
        # Implementação da lógica recursiva
        if p_node is None and q_node is None:
            return True
        
        # NOTE: Se você manteve 'data' no seu Node, use p_node.data != q_node.data
        if p_node is None or q_node is None or p_node.data != q_node.data:
            return False
            
        return (self._isSameTree_recursive(p_node.left, q_node.left) and 
                self._isSameTree_recursive(p_node.right, q_node.right))

class BinarySearchTree(BinaryTree):
    
    def insert(self, value):
        parent = None
        x = self.root
        while(x):
            parent = x
            if value < x.data:
                x = x.left
            else:
                x = x.right
        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, node):
        if node is None:
            return node
        if node.data == value:
            return BinarySearchTree(node)
        if value < node.data:
            return self._search(value, node.left)
        return self._search(value, node.right)

    def min(self, node=ROOT):
        if node == ROOT:
            node = self.root
        while node.left:
            node = node.left
        return node.data

    def max(self, node=ROOT):
        if node == ROOT:
            node = self.root
        while node.right:
            node = node.right
        return node.data

    def remove(self, value, node=ROOT):
        if node == ROOT:
            node = self.root
        if node is None:
            return node
        if value < node.data:
            node.left = self.remove(value, node.left)
        elif value > node.data:
            node.right = self.remove(value, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                substitute = self.min(node.right)
                node.data = substitute
                node.right = self.remove(substitute, node.right)

        return node


if __name__ == "__main__":

    random.seed(77)

    lista = random.sample(range(1, 11), 10)
    arvore = BinarySearchTree()

    for i in lista:
        arvore.insert(i)

    arvore.inorder_traversal()

    itens = [1, 2, 3, 11]

    for item in itens:
        i = arvore.search(item)
        if i is None:
            print(f'\n{item} não encontrado')
        else:
            print(f'\n{i.root.data} encontrado')






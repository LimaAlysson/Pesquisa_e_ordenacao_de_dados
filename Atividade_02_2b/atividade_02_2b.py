#Equipe
# Alysson José - André Vasconcelos - Leonardo Lucena

class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
            
        esquerda_igual = self.isSameTree(p.left, q.left)
        direita_igual = self.isSameTree(p.right, q.right)
        return esquerda_igual and direita_igual
# Equipe: Alysson José e Leonardo Lucena
# leetcode problem: height-checker

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        n = len(heights)
        maior = 0

        for i in heights:
            if i > maior:
                maior = i

        contagem = [0] * (maior+1)

        for j in heights:
            contagem[j] += 1

        for k in range(1, maior+1):
            contagem[k] += contagem[k-1]

        saida = [0] * n 

        for k in range(n-1, -1, -1):
            v = heights[k]
            saida[contagem[v] - 1] = v
            contagem[v] -= 1
            
        cont = 0

        for l in range(n):
            if saida[l] != heights[l]:
                cont += 1
        
        return cont
        
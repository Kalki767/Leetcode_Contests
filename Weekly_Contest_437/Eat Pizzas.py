import math
from typing import List


class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        answer = 0
        pizzas.sort(reverse = True)
        total = int(len(pizzas)/4)
        odd = int(math.ceil(total/2))
        even = total//2
        for i in range(odd):
            answer += pizzas[i]
        for i in range(odd + 1, len(pizzas),2):
            if even == 0:
                break
            answer += pizzas[i]
            even -= 1
            
        return answer
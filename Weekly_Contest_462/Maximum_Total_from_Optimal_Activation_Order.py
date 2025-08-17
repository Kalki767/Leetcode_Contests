from collections import defaultdict
from typing import List


class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        '''Approach: Dictionary based iteration'''
        merged = list(zip(value,limit))
        merged.sort(key = lambda x : x[1])
        sorted_values = defaultdict(list)
        counter = defaultdict(int)
        for val, lim in merged:
            sorted_values[lim].append(val)
        
        for key in sorted_values:
            sorted_values[key].sort(reverse = True)

        # print(sorted_values)   
        total = active = 0
        for key in sorted_values:
            for val in sorted_values[key]:
                if key > active:
                    active += 1
                    counter[key] += 1
                    total += val
                    # print(active,total)
                    if key <= active:
                        active = 0
                        counter[key] = 0
                        break
                    else:
                        prev_active = active
                        active -= counter[active]
                        counter[prev_active] = 0
                        if active >= key:
                            break
                            
        
        return total
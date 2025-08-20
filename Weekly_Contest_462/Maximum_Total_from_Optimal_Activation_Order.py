from collections import defaultdict
from typing import List


class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        '''Approach: Dictionary based iteration. The problem asks to calculate the total activation value that
        we can obtain if we use the optimal way. Here we are given a set of rules. The first one is a value
        can only be activated if it's limit is strictly less than the limit. and after activation all elements
        those which are active and inactive whose limit is less than or equal to the current active elements
        will become permanently inactive. This tells us something when an element that was active becomes inactive
        it decreases the number of active elements. Now from the rules for the first rule since at the start our
        active elements are 0 we should start with an element that has the smaller number of limit so that we
        can immediately activate it. We can keep doing this and if after each activation if the limit of
        the current element is equal to the active elements then we make the number of the active elements
        set to 0 because we are moving in ascending order and every active element before it has a limit less
        than it. But here comes a confusing thing what if we have elements who have the same limit. If at some
        point the limit and the current active element become equal then all of them will be permanently inactive
        avoiding us to move any further. This means for values that have the same limit we should start from the
        maximum and move down. Another issue is at every point even if the current limit is still greater than
        the active elements there might be a previous element whose limit is equal to active elements for that
        matter we are tracking the number of active elements at every limit in a dictionary and updating it as
        we move.'''

        #Step1: zip the value and the limit and sort it based on the limit
        merged = list(zip(value,limit))
        merged.sort(key = lambda x : x[1])

        #Step2: create a dictionary to hold the values that have the same limit together so it's easier to traverse through them
        sorted_values = defaultdict(list)
        counter = defaultdict(int)
        for val, lim in merged:
            sorted_values[lim].append(val)
        
        #Step3: sort the values in each of the limits in reverse order to get the maximum one first
        for key in sorted_values:
            sorted_values[key].sort(reverse = True)

        #Step4: Traverse through the dictionary on each limit and perform the explained operation  
        total = active = 0
        for key in sorted_values:
            for val in sorted_values[key]:
                if key > active: #if it satisfies the rule activate the value which increases the no of active elements by 1
                    active += 1
                    counter[key] += 1
                    total += val
                    if key <= active: #if the limit is less or equal to the no of active elements reset it to 0 and break out because all elements with the same limit have become permanently inactive
                        active = 0
                        counter[key] = 0
                        break
                    else:
                        prev_active = active #hold the no of active elements in different variable
                        active -= counter[active] #decrement the no of active elements by the no of active elements before it that were store previusly
                        counter[prev_active] = 0 #set this one to zero as they have all become inactive
                        if active >= key: #if the active is greater than equal to limit break it
                            break
                            
        return total
        #Time Complexity: O(nlogn) for sorting every values
        #Space Complexity: O(n+m) for the dictionary and for the list
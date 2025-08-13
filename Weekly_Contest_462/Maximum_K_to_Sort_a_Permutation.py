from typing import List


class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        '''Approach: Bitwise AND. The problem asks to find the maximum k such that
        two elements can be swapped when their and result is equal to k and we can
        sort the input. Here let's look at the problem a little closer. The first
        useful thing that we have is the array is a permutation from 0 to n-1 which
        means from this we can know the final position of each element by matching
        it with the index. Another clue is if an element is already in it's final
        position there is no need to swap it with any element to sort the array.
        Now if the index and the value at that index doesn't match that means a
        different value is there that needs to be swapped. We can swap it with the
        correct value if and only if we find the and result of the index and value
        and take that as a k. But what if we have multiple elements which are not in
        their final position? that means we are going to have multiple k's but we
        need only one k so we need to take the and of all those k's. Why would this
        work? Instead of swapping with the direct element at the required position
        we can also swap them with another element and continue swapping as long as
        the condition is satisfied and the array is not sorted. Because there is no
        restriction on the number of swap that can be made.'''

        ans = float('inf')
        for i in range(len(nums)):
            if nums[i] == i:
                continue
            bitwise_and = nums[i] & i
            if ans == float('inf'):
                ans = bitwise_and
            else:
                ans = ans & bitwise_and
        
        return ans if ans != float('inf') else 0
        #Time Complexity: O(n)
        #Space Complexity: O(1)
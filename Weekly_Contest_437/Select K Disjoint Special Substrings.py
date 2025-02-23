from collections import Counter, defaultdict


class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        if k == 0:
            return True
        counter = Counter(s)
        if len(counter) < k:
            return False

        intervals = defaultdict(list)
        visited = set()
        for i in range(len(s)):
            if s[i] not in visited:
                visited.add(s[i])
                intervals[s[i]].append(i)

        visited = set()
        for i in range(len(s)-1,-1,-1):
            if s[i] not in visited:
                visited.add(s[i])
                intervals[s[i]].append(i)

        interval_list = [(val) for key, val in intervals.items()]
        interval_list.sort(key = lambda x: x[1])
        cur_count = 0
        cur_end = -1
        for start, end in interval_list:
            if start > cur_end:
                cur_end = end
                cur_count += 1
        
        return cur_count >= k

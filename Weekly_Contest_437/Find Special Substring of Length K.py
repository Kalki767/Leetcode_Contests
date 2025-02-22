class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        index = 0
        while index < len(s):
            counter = 1
            index += 1
            while index < len(s) and s[index] == s[index-1]:
                counter += 1
                index += 1
            if counter == k:
                return True
        return False
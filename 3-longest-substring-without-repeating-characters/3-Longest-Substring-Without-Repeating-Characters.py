class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        exists = []
        maximum = 0
        for x in s:
            if x in exists:
                exists = exists[exists.index(x) + 1:]
            exists.append(x)
            maximum = max(maximum, len(exists))
        return maximum
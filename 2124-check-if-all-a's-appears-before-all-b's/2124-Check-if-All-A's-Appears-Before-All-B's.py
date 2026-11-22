class Solution:
    def checkString(self, s: str) -> bool:
        if 'a' not in s:
            return True
        seen = False
        for x in s:
            if x is 'a':
                if not seen:
                    continue
                else:
                    return False
            if x is 'b':
                seen = True
        return True
        
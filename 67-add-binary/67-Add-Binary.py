class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y= [],[]
        for i in a:
            x.append(int(i)) 
        for i in b:
            y.append(int(i)) 
        n = int(''.join(map(str, x)), 2)
        m = int(''.join(map(str, y)), 2)

        return str(bin(n+m))[2:]
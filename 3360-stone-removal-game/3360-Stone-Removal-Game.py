class Solution:
    def canAliceWin(self, n: int) -> bool:
        alice = 10
        bob = 9
        while(True):
            n = n - alice
            if(n < 0):
                return False
            n = n - bob
            if(n<0):
                return True
            alice, bob = alice - 2, bob - 2
        
        
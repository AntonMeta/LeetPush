class Solution {
public:
    int mySqrt(int x) {
        long long n = 1;
        while(n*n != x){
            if(n*n>x)
                return n-1;
            n++;
        }
        return n;
    }
};
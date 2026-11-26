class Solution {
public:
    double myPow(double x, int n) {
        double tmp = x;
        double wynik = 1;
        long long m = n;
        if(n==0 || x == 1)
            return 1;
        if ( x == -1){
            if(n %2 == 0)
                return 1;
            else
                return -1;
        }
        if(n>0){

            while(m > 0){
                if(m %2 == 1)
                    wynik *= tmp;
                tmp *= tmp;
                m /= 2;
            }
            return wynik;
        }
        else{

            m = -m;
            while(m > 0){
                if(m %2 == 1)
                    wynik *= tmp;
                tmp *= tmp;
                m /= 2;
            }
            return 1/wynik;
        }

    }
};
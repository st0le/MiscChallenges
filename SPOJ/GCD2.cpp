#include <cstdio>
using namespace std;

int gcd(int a,int b){
    while(b){
        int c = a % b;
        a = b;
        b = c;
    }
    return a;
}

int main(){
    
    int t,a,_b ;
    scanf("%d",&t);
    char b[300];
    while(t-->0){
        _b = 0;
        scanf("%d %s",&a,b);
        if(a == 0){
            printf("%s\n",b);
        }else{
            for(int i = 0; b[i]; i++){
                _b = _b * 10 + b[i] - '0';
                if(_b > a){
                    _b = _b % a;
                }
            }
            printf("%d\n",gcd(a,_b));
        }
    }
    return 0;
}
#include <cstdio>
using namespace std;

int eval(char c){
    switch(c){
        case 'm': return 1000;
        case 'c': return 100;
        case 'x': return 10;
        case 'i': return 1;
    }
    return c - '0';
}

int toInt(char *mcxi){
    int s = 0;
    while(*mcxi){
        char c = *mcxi;
        if(c >= '2' && c <= '9'){
            s += eval(c) * eval(*(mcxi+1));
            mcxi+=2;
        }else{
            s += eval(c);
            mcxi++;
        }
    }
    return s;
}

char * toMCXI(int n,char *s){
    char *f = "mcxi";
    int j = 0;
    int p = 1000;
    char *a = s;
    *a = 0;
    while(p > 0){
        int d = (n / p) % 10;
        if(d >= 1){
            if(d > 1){
                *a = d + '0';
                a++;
            }
            *a = f[j];
            a++;
        }
        *a = 0;
        j++;
        p /= 10;
    }
    *a = 0;
    return s;
}

int main(){
    
    int t;
    char a[10],b[10],c[10];
    for(scanf("%d",&t); t-- > 0; ){
        scanf("%s %s",a,b);
        printf("%s\n",toMCXI(toInt(a)+toInt(b),c));
    }
    return 0;
}
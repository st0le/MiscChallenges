#include <cstdio>

using namespace std;
const int N = 101;
int fact[N][1000];
int len[N];


void init(){
    
    fact[0][len[0]++] = 1;
    for(int i = 1; i < N; i++){
        //fact[i] = i * fact[i-1]
        int c = 0,j;
        for(j = 0; j < len[i-1]; j++){
            int p = fact[i-1][j] * i + c;
            fact[i][j] = p % 10;
            c = p/10;
        }
        while(c > 0){
            fact[i][j++] = c % 10;
            c /= 10;
        }
        len[i] = j;
    }
}

void printFactorial(int n)
{
    for(int i = len[n] - 1; i >= 0; i--){
        printf("%d",fact[n][i]);
    }
    printf("\n");
}

int main(){
    int t,n;
    init();
    for(scanf("%d",&t); t>0; t--){
        scanf("%d",&n);
        printFactorial(n);
    }
    return 0;
}
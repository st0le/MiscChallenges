#include <cstdio>

using namespace std;

int powCount(int n,int k){
    int c = 0;
    while(n > 0){
        c += n /= k;
    }
    return c;
}

int main(){
    int t,n;
    for(scanf("%d",&t); t>0; t--){
        scanf("%d",&n);
        printf("%d\n",powCount(n,5));
    }
    return 0;
}
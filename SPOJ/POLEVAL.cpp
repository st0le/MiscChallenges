#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    
    int n,m,x,t = 0;
    int c[1000];
    
    while(true){
        scanf("%d",&n);
        if(n == -1) break;
        printf("Case %d:\n",++t);
        for(int i = n ; i >= 0 ; i--)
            scanf("%d",&c[i]);
        scanf("%d",&m);
        for(int i = 0 ; i < m; i++){
            scanf("%d",&x);
            long s = 0;
            for(int j = n; j >= 0; j--)
                s = s * x + c[j];
            printf("%ld\n",s);
        }
    }
    return 0;
}
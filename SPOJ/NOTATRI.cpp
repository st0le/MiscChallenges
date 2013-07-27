#include <cstdio>
#include <algorithm>
using namespace std;

int main(){
    
    int n;
    int arr[2000 + 1];
    while(true){
        scanf("%d",&n);
        if(n == 0) break;
        for(int i = 0; i < n; i++)
            scanf("%d",&arr[i]);
        sort(arr,arr+n);
        int c = 0;
        for(int i = 0; i < n; i++)
            for(int j = i + 1; j < n; j++)
                c += (arr + n) - upper_bound(arr + j, arr+n, arr[i] + arr[j]);
        printf("%d\n",c);
    }
    
    return 0;
}
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int t,a,b,c,d;
    scanf("%d",&t);
    vector<int> A,B,C,D;
    for(int i = 0; i < t; i++){
        scanf("%d%d%d%d",&a,&b,&c,&d);
        A.push_back(a);
        B.push_back(b);
        C.push_back(c);
        D.push_back(d);
    }
    vector<int> AB,CD;
    for(int i = 0; i < t; i++){
        for(int j = 0; j < t; j++){
            AB.push_back(A[i]+B[j]);
            CD.push_back(C[i]+D[j]);
        }
    }
    sort(AB.begin(),AB.end());
    sort(CD.begin(),CD.end());
    
    int cnt = 0,k = t*t;
    int left = 0, right = t*t - 1;
    while(left < k && right >= 0){
        int s = AB[left] + CD[right];
        
        if(s == 0){
            
            int i = left + 1, j = right - 1;
            while(i < k && AB[i] == AB[left]) i++;
            while(j >= 0 && CD[j] == CD[right]) j--;
            cnt += (i - left) * (right - j);
            left = i;
            right = j;
        }else if(s < 0)
            left ++;
        else
            right--;
    }
    printf("%d\n",cnt);
    return 0;
}
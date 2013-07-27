#include <cstdio>

using namespace std;

char * next_palidrome(char *num){
    
    int len = 0;
    while(num[len]) len++;
    int i = len / 2, j = len / 2;
    if (len % 2 == 0) i --;
    int p  = i, q = j;
    while( p >= 0 && num[p] == num[q]){
        p--,q++;
    }
    if ( p < 0 || num[p] < num[q]){
        while(i >= 0){
            if(num[i] == '9'){
                num[i] = num[j] = '0';
            }else{
                num[i] = num[j] = num[i] + 1;
                break;
            }
            i--,j++;
        }
    }
    while (p >= 0){
        num[q] = num[p];
        p--,q++;
    }
    if(num[0] == '0'){
        num--;
        num[0] = num[len] = '1';
    }
    return num;
}

int main(){
    int n;
    const int K = 1000000 + 10;
    char num[K];
    scanf("%d",&n);
    while(n--){
        num[0] = 0;
        scanf("%s",num+1);
        printf("%s\n",next_palidrome(num+1));
    }
    return 0;
}
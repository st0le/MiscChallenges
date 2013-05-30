// (c) st0le
#include <stdio.h>
#define get_c getchar
typedef unsigned int type;

void next_int(type *n){
    register char c = 0;
    while((c = get_c()) < 33);
    *n = 0;
    
    do{
        *n = *n * 10 + c - '0';
    }while((c = get_c()) > 33);
    
}

int main(){
	type T,K,N,C=0;
    next_int(&T);
    next_int(&K);
    
    while(T--)
    {
        next_int(&N);
        if(N % K == 0)
            C++;
    }
    printf("%u\n",C);
	return 0;
}
// (c) st0le
#include <stdio.h>
#define MAX (101)
char factorial[MAX][300];
int len[MAX];


int main(){
	int t,n,i,j;
	
	factorial[0][0] = 1;
	factorial[0][1] = 0;
	len[0] = 1;
	for( i = 1; i < MAX; i++)
	{
		int c = 0;
		for(j = 0; j < len[i-1]; j++){
			c = i * factorial[i-1][j] + c;
			factorial[i][j] = c % 10;
			c = c / 10;
		}
		while(c > 0){
			factorial[i][j++] = c % 10;
			c = c / 10;
		}
		len[i] = j;
		
	}
	
	scanf("%d",&t);
	while(t-->0){
		scanf("%d",&n);
		for(i = len[n] - 1; i >= 0; i-- )
			printf("%d",factorial[n][i]);
		printf("\n");
	}
	return 0;
}
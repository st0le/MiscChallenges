#include <stdio.h>

int main(){
	int n,t,c;
	scanf("%d",&t);
	while(t-->0){
		scanf("%d",&n);
		c = 0;
		while(n > 0)
		{
			n /= 5;
			c += n;
		}
		printf("%d\n",c);
	}
	return 0;
}
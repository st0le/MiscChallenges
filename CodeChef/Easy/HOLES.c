// (c) st0le
#include <stdio.h>

int main(){
	
	char line[110];
	int i,T;
	scanf("%d",&T);
	while(T-->0)
	{
		scanf("%s",line);
		int c = 0;
		for( i = 0 ; line[i]; i++)
		{
			switch(line[i])
			{
			case 'B':
				c++;
			case 'A':
			case 'D':
			case 'O':
			case 'P':
			case 'Q':
			case 'R':
				c++;
				break;
			}
		}
		printf("%d\n",c);
	}
	
	return 0;
}
// (c) st0le
#include <stdio.h>
#include <map>
using namespace std;
typedef unsigned long long ULL;

map<ULL, ULL> cache;

ULL coins(ULL n){
	if(cache.find(n) == cache.end())
		return cache[n] = max( n, coins(n/2) + coins(n/3) + coins(n/4));
	return cache[n];
}

int main(){
	ULL n;
	cache[0] = 0;
	while(scanf("%llu",&n) > 0){
		printf("%llu\n",coins(n));
	}
	return 0;
}
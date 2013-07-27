#include <cstdio>

using namespace std;

int main(){
    long long n;
    scanf("%lld",&n);
    printf("%s\n",n <= 1 || ((n & (n - 1)) == 0) ? "TAK" : "NIE");
    return 0;
}
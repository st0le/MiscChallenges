#include <iostream>
#include <map>
#include <cstdio>
using namespace std;

int main(){
    
    int m,n;
    while(true){
        map<string,int> hash;
        map<int,int> freq;
        string s;
        scanf("%d %d",&m,&n);
        if(m == 0 && n == 0) break;
        for(int i = 0 ; i < m; i++)
        {
            cin>>s;
            ++hash[s];
        }
        for(map<string,int>::iterator itr = hash.begin(); itr != hash.end(); itr++){
            //printf("%s %d\n",itr->first.c_str(),itr->second);
            freq[itr->second] ++;
        }
        
        for(int i = 1; i <= m; i++)
            printf("%d\n",freq[i]);
    }
    return 0;
}
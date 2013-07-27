#include <cstdio>
#include <vector>
#include <queue>
using namespace std;
typedef pair<int,int> pii;
typedef vector<vector<pii>> graph;
const int INF = (1<<28);

int dijkstra(graph &g,int src,int dst){
    int V = g.size() - 1;
    vector<int> d(V + 1, INF);
    priority_queue<pii,vector<pii>,greater<pii>> pq;
    pq.push(make_pair(d[src] = 0,src));
    while(!pq.empty()){
        int u = pq.top().second;
        pq.pop();
        if(u == dst) break;
        for(int vi = 0,sz = g[u].size(); vi < sz; vi++){
            int v = g[u][vi].first, w = g[u][vi].second;
            if(d[u] + w < d[v]){
                d[v] = d[u] + w;
                pq.push(make_pair(d[v],v));
            }
        }
    }
    return d[dst];
}

graph input_graph(){
    int E,V,u,v,w;
    scanf("%d %d",&V,&E);
    graph g(V+1);
    for(int i = 0; i < E; i++){
        scanf("%d%d%d",&u,&v,&w);
        g[u].push_back(make_pair(v,w));
    }
    return g;
}

int main(){
    int t,src,dst;
    scanf("%d",&t);
    while(t-->0){
        graph g = input_graph();
        scanf("%d %d",&src,&dst);
        int d = dijkstra(g,src,dst);
        if(d == INF){
            printf("NO\n");
        }else{
            printf("%d\n",d);
        }
    }
    return 0;
}
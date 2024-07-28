class Solution
{
public:
    int secondMinimum(int n, vector<vector<int>> &edges, int time, int change)
    {
        vector<vector<int>> adj(n + 1);
        for (int x = 0; x < edges.size(); x++)
        {
            adj[edges[x][0]].push_back(edges[x][1]);
            adj[edges[x][1]].push_back(edges[x][0]);
        }

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        vector<pair<int, int>> dist(n + 1, {1e9, 1e9});
        pq.push({0, 1});
        dist[1].first = 0;
        while (!pq.empty())
        {

            pair<int, int> node = pq.top();

            pq.pop();
            int d = node.first;
            int nd = node.second;
            int i = 0;

            if (d < change)
            {
                i = time;
            }
            else if (d >= change && (d / change) % 2 == 0)
            {
                i = time;
            }
            else if (d >= change && (d / change) % 2 == 1)
            {
                i = time + change - (d % change);
            }

            for (auto j : adj[nd])
            {
                if (i + d < dist[j].first)
                {
                    dist[j].first = i + d;
                    pq.push({dist[j].first, j});
                }
                else if (i + d > dist[j].first && i + d < dist[j].second)
                {
                    dist[j].second = i + d;
                    pq.push({dist[j].second, j});
                }
            }
        }
        return dist[n].second;
    }
};
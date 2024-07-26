class Solution
{
public:
    int n, distanceThreshold;
    int dist[100][100];
    void FloydWarshall(vector<vector<int>> &edges)
    {
        fill(&dist[0][0], &dist[0][0] + 100 * 100, 1e9);
        for (int i = 0; i < n; i++)
            dist[i][i] = 0;
        for (auto &e : edges)
        {
            int u = e[0], v = e[1], w = e[2];
            if (w <= distanceThreshold)
                dist[u][v] = dist[v][u] = w;
        }
        for (int k = 0; k < n; k++)
        {
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }
    int findTheCity(int n, vector<vector<int>> &edges, int distanceThreshold)
    {
        this->n = n;
        this->distanceThreshold = distanceThreshold;
        FloydWarshall(edges);

        int min_count = n, city = -1;
        for (int i = 0; i < n; i++)
        {
            int count = count_if(&dist[i][0], &dist[i][0] + n, [&](int x)
                                 { return x <= distanceThreshold; }) -
                        1;
            if (count <= min_count)
            {
                min_count = count;
                city = i;
            }
        }
        return city;
    }
};
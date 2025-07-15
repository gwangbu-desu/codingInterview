#include <bits/stdc++.h>
#include <unordered_map>

using namespace std;
//pq sort 방법 priority_queue<int,vector<int>,greater<int>> 
int arr[1001][1001];
bool visited[1001][1001];
int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int n, m;
	int k;
	queue<pair<int, int>> q;
	cin >> n >> m;
	for (int j = 0; j < m; j++) {
		for (int i = 0; i < n; i++) {
			cin >> k;
			if (k == 1) {
				arr[i][j] = 1;
				visited[i][j] = 1;
				q.push(make_pair(i, j));
			}
			else if (k == -1) {
				arr[i][j] = -1;
				visited[i][j] = 1;
			}
		}
	}
	int day = 0;
	int nx, ny;
	pair<int, int> a;
	int flag = 1;
	if (q.empty()) flag = 0;
	while (!q.empty()) {
		a = q.front();
		q.pop();
		day = arr[a.first][a.second];
		for (int i = 0; i < 4; i++) {
			nx = a.first + dx[i], ny = a.second + dy[i];
			if (nx >= 0 && ny >= 0 && nx < n && ny < m && !visited[nx][ny]&&arr[a.first][a.second]>=1) {
				q.push(make_pair(nx, ny));
				arr[nx][ny] = day + 1;
				visited[nx][ny] = 1;
			}
		}
	}

	for (int j = 0; j < m; j++) {
		for (int i = 0; i < n; i++) {
			if (arr[i][j] == 0) {
				flag = -1;
				//break;
			}
		}
	}
	if (flag == -1) cout << flag;
	else if (flag == 0) cout << flag;
	else cout << day - 1;
	
}
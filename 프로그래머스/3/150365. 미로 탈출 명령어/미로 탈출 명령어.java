import java.util.*;

class Solution {
    int[] dr = {1, 0, 0, -1};  // d, l, r, u
    int[] dc = {0, -1, 1, 0};
    char[] dirChar = {'d', 'l', 'r', 'u'};
    int N, M, K;
    String answer = "impossible";
    boolean found = false;

    public String solution(int n, int m, int x, int y, int r, int c, int k) {
        N = n;
        M = m;
        K = k;
        
        int dist = Math.abs(x - r) + Math.abs(y - c);
        if (dist > k || (k - dist) % 2 != 0) return "impossible";

        dfs(x, y, r, c, 0, "");
        return answer;
    }

    void dfs(int r, int c, int tr, int tc, int cnt, String path) {
        if (found) return;

        int remain = K - cnt;
        int minDist = Math.abs(r - tr) + Math.abs(c - tc);
        if (minDist > remain || (remain - minDist) % 2 != 0) return;

        if (cnt == K) {
            if (r == tr && c == tc) {
                answer = path;
                found = true;
            }
            return;
        }

        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d];
            int nc = c + dc[d];

            if (nr < 1 || nc < 1 || nr > N || nc > M) continue;

            dfs(nr, nc, tr, tc, cnt + 1, path + dirChar[d]);
            if (found) return;
        }
    }
}

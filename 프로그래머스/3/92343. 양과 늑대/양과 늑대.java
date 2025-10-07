import java.util.*;

class Solution {
    int answer = 0;
    ArrayList<Integer>[] tree;

    public int solution(int[] info, int[][] edges) {
        int n = info.length;
        tree = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            tree[i] = new ArrayList<>();
        }

        for (int[] e : edges) {
            tree[e[0]].add(e[1]);
        }

        // 루트(0번)에서 시작
        dfs(0, 0, 0, new ArrayList<>(), info);
        return answer;
    }

    void dfs(int node, int sheep, int wolf, List<Integer> nextNodes, int[] info) {
        if (info[node] == 0) sheep++;
        else wolf++;

        // 조건 위반 시 종료
        if (wolf >= sheep) return;

        // 최대 양 개수 갱신
        answer = Math.max(answer, sheep);

        // 현재 node의 자식들을 후보 리스트에 추가
        List<Integer> candidates = new ArrayList<>(nextNodes);
        candidates.remove(Integer.valueOf(node));
        candidates.addAll(tree[node]);

        for (int next : candidates) {
            dfs(next, sheep, wolf, candidates, info);
        }
    }
}

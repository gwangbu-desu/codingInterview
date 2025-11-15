import java.util.*;

class Solution {
    HashSet<Integer> trapSet = new HashSet<>();
    ArrayList<int[]>[] edges;

    public int solution(int n, int start, int end, int[][] roads, int[] traps) {

        for (int t : traps) trapSet.add(t);

        edges = new ArrayList[n+1];
        for (int i = 1; i <= n; i++) edges[i] = new ArrayList<>();

        for (int[] r : roads) {
            edges[r[0]].add(new int[]{r[1], r[2], 0}); // 정방향
            edges[r[1]].add(new int[]{r[0], r[2], 1}); // 역방향
        }

        // 트랩 인덱스 매핑 (node 번호 → trap bit 위치)
        Map<Integer, Integer> trapIndex = new HashMap<>();
        for (int i = 0; i < traps.length; i++) {
            trapIndex.put(traps[i], i);
        }

        int maxState = 1 << traps.length;
        int[][] dist = new int[n+1][maxState];
        for (int i = 0; i <= n; i++) Arrays.fill(dist[i], Integer.MAX_VALUE);

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        pq.offer(new int[]{0, start, 0}); // cost, node, state
        dist[start][0] = 0;

        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int curCost = cur[0];
            int curNode = cur[1];
            int curState = cur[2];

            // 이미 더 나은 경로가 있다면 skip
            if (dist[curNode][curState] < curCost) continue;
            if (curNode == end) return curCost;

            // 현재 노드 트랩 활성 여부
            boolean curActive = false;
            if (trapIndex.containsKey(curNode)) {
                curActive = ((curState & (1 << trapIndex.get(curNode))) != 0);
            }

            for (int[] edge : edges[curNode]) {
                int nextNode = edge[0];
                int w = edge[1];
                int direction = edge[2];

                // 다음 노드가 트랩인지 여부
                boolean nextActive = false;
                if (trapIndex.containsKey(nextNode)) {
                    nextActive = ((curState & (1 << trapIndex.get(nextNode))) != 0);
                }

                // 두 트랩 ON 상태 개수의 홀/짝 판단 = XOR 사용
                boolean isReversed = curActive ^ nextActive;

                // ❗ 방향 판정
                if (!isReversed && direction == 1) continue;
                if (isReversed && direction == 0) continue;

                //다음 상태 계산 (트랩이면 ON/OFF 토글)
                int nextState = curState;
                if (trapIndex.containsKey(nextNode)) {
                    nextState ^= (1 << trapIndex.get(nextNode));
                }

                int nextCost = curCost + w;

                // 이미 더 짧은 비용이 있으면 PQ에 넣지 않음
                if (nextCost < dist[nextNode][nextState]) {
                    dist[nextNode][nextState] = nextCost;
                    pq.offer(new int[]{nextCost, nextNode, nextState});
                }
            }
        }
        return -1;
    }
}

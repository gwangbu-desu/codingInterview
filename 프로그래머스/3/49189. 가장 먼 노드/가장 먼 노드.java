import java.util.*;
class Solution {
    public int solution(int n, int[][] edge) {
        
        int[] distance  = new int[n+1]; // 1-th index
        boolean[] visited = new boolean[n+1];
        ArrayList<Integer>[] edges = new ArrayList[n+1];
        int answer = 0;
        
        for(int i = 0;i<=n;i++){ // 간선 담을 배열
            edges[i] = new ArrayList<>();
        }
        for(int[] _edge : edge){
            edges[_edge[0]].add(_edge[1]);
            edges[_edge[1]].add(_edge[0]);
        }
        Queue<Integer> dq = new ArrayDeque<>();
        dq.add(1);
        visited[1] = true;
        while(!dq.isEmpty()){
            int temp = dq.poll();
            for(Integer dist: edges[temp]){ // 
                if(visited[dist]) continue; // 방문한곳 = 최단 거리가 구해진곳은 건너뛰기.
                visited[dist] = true;
                dq.add(dist);
                distance[dist] = distance[temp] + 1;
                
            }
        }
        Arrays.sort(distance);
        int max = distance[n];
        // System.out.println(max);
        for(int i: distance){
            System.out.println(i);
            if ( i == max){
                answer ++;
            }
        }
        return answer;
    }
}
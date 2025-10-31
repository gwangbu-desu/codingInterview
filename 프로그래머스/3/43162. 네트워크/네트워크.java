import java.util.*;

class Solution {
    public boolean[] visited;
    public int solution(int n, int[][] computers) {
        int answer = 0;
        visited = new boolean[n]; 
        for(int i=0;i<n;i++){
            if(!visited[i]){ // 방문하지 않았을때
                bfs(computers, n, i);
                answer ++;
            }
        }
        // Arrays.count(visited,false)
        return answer;
    }
    public void bfs(int[][] map, int n, int start){
        ArrayDeque<Integer> dq = new ArrayDeque<>();
        visited[start] = true;
        dq.add(start);
        while(!dq.isEmpty()){
            int temp = dq.poll();
            for(int i=0;i<n;i++){
                if(!visited[i] && map[temp][i] == 1) {
                    dq.add(i);
                    visited[i] = true;
                }
            }
        }
    }
    
}
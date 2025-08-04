import java.util.*;

class Solution {
    ArrayList<ArrayList<Integer>> adj_graph = new ArrayList<>();
    boolean[] visited = new boolean[20001];
    int[] distance = new int[20001];
    public void start(){
        int start = 1;
        int start_length = 0;
        Integer node;
        Integer next_node;
        ArrayList<Integer> graph;
        Arrays.fill(distance,50000);
        distance[1] = 0;
        ArrayDeque<Integer> dq = new ArrayDeque<>(); //길이, 노드
        dq.add(1);
        while(!dq.isEmpty()){
            node = dq.poll();
            graph = adj_graph.get(node);
            for(int i=0;i<graph.size();i++){
                next_node = graph.get(i); // 다음 방문 노드
                if(distance[next_node] > distance[node] + 1){
                    distance[next_node] = distance[node] + 1;                
                    dq.add(next_node);
                }
            }
        }
    }
    public int solution(int n, int[][] edge) {
        int answer = 0;
        for(int i=0;i<=n;i++){
            adj_graph.add(new ArrayList<>());
        }
        for(int[] each_edge:edge){
            adj_graph.get(each_edge[1]).add(each_edge[0]);
            adj_graph.get(each_edge[0]).add(each_edge[1]);
        }
        
        start();
        int maximum=0;
        int count=0;
        for(int i=0;i<20001;i++){
            if(distance[i] == 50000){
                continue;
            }
            
            // System.out.print(distance[i]);
            if(distance[i] > maximum){
                maximum = distance[i];
                answer = 1;
            }else if(distance[i] == maximum){
                answer+=1;
            }
        }
        // System.out.println(count);
        return answer;
    }
}
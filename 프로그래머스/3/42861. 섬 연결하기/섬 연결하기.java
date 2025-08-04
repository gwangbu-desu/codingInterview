import java.util.*;

class Solution {
    public int[] parents;
    public int find_parent(int a){
        if (parents[a] != a){
            parents[a] = find_parent(parents[a]);
        }
        return parents[a];
    }
    public int solution(int n, int[][] costs) {
        int answer = 0;
        parents = new int[n];
        for(int i=0;i<n;i++){
            parents[i] = i;
        }
        Arrays.sort(costs, (a,b) -> a[2] - b[2]);
        int parentA, parentB;
        for(int[] cost: costs){
            parentA = find_parent(cost[0]);
            parentB = find_parent(cost[1]);
            if( parentA == parentB){
                continue;
            }else if (parentA > parentB){
                parents[parentA] = parentB;
                answer += cost[2];
            }else{
                parents[parentB] = parentA;
                answer += cost[2];
            }
        }
        return answer;
    }
}
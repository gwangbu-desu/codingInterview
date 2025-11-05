import java.util.*;
class Solution {
    public int solution(int[][] routes) {
        int answer = 0;
        Arrays.sort(routes,(a,b)->a[1] - b[1]);
        int end = -30001;
        for(int[] route : routes){
            // System.out.printf("%d, %d\n", route[0], route[1]);
            if(route[0] > end){
                end = route[1];
                answer ++;
            }
            
        }
        return answer;
    }
}
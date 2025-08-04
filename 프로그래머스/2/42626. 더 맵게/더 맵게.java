import java.util.*;
class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b) -> a-b);
        for(int tmp : scoville){
            pq.add(tmp);
        }
        while(pq.size() > 1 &&pq.peek() < K){
            int low = pq.poll();
            int high = pq.poll();
            int mix = low + high * 2;
            pq.add(mix);
            answer ++;
        }
        if (pq.peek() < K){
            answer = -1;
        }
        
        return answer;
    }
}
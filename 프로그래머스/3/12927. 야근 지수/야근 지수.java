import java.util.*;

class Solution {
    public long solution(int n, int[] works) {
        long answer = 0;
        // 내림차순 정렬
        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b) -> b-a);
        for(int work:works) pq.add(work);
        System.out.println(pq.peek());
        for(int i=0;i<n;i++){
            if(pq.isEmpty()) break;
            if(pq.peek() == 0) break;
            pq.add(pq.poll()-1);
        }
        while(!pq.isEmpty()){
            int a = pq.poll();
            answer += a * a;
        }
        return answer;
    }
}
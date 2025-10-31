import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        int[] answer = {};
        PriorityQueue<Integer> pq_min = new PriorityQueue<>((a,b) -> a-b);
        
        PriorityQueue<Integer> pq_max = new PriorityQueue<>((a,b) -> b-a);
        for(String i : operations){
            StringTokenizer st = new StringTokenizer(i);
            String command = st.nextToken();
            int value = Integer.parseInt(st.nextToken());
            if(command.equals("I")){
                pq_min.add(value);
                pq_max.add(value);
            }else{
                if(pq_min.isEmpty()) continue;
                if(value == -1){
                    int target = pq_min.poll();
                    pq_max.remove(target);
                }else{
                    int target = pq_max.poll();
                    pq_min.remove(target);
                }
            }
        }
        answer = new int[2];
        if(!pq_max.isEmpty()){
            answer[0] = pq_max.poll();
            answer[1] = pq_min.poll();
        }
        return answer;
    }
}
import java.util.*;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        LinkedList<String> cache = new LinkedList<>();
        for(String city : cities){
            
            String lower = city.toLowerCase();
            if (!cache.isEmpty()){
                // hit -> 해당 요소 제거
                if(cache.contains(lower)){
                    answer ++;
                    if(cache.size() == cacheSize){
                        cache.remove(lower);
                    }
                    // miss -> 첫 요소 제거
                }else{
                    answer += 5;
                    if (cache.size() == cacheSize){
                        cache.poll();    
                    }
                }
            }else{
                answer += 5;
            }
            if (cacheSize > 0){
                    cache.offer(lower);
                }
        }
        return answer;
    }
}
import java.util.*;

class Solution {
    public int solution(int n, int[] stations, int w) {
        int answer = 0;
        int pos = 1;
        int idx = 0;
        while(pos <= n){
            if(idx < stations.length && stations[idx] - w <= pos ){
                pos = stations[idx] + w + 1;
                idx ++;
            }else{
                answer ++;
                pos += w*2 + 1;
            }
        }
        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        // System.out.println("Hello Java");
        
        return answer;
    }
}
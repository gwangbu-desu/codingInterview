import java.util.*;
class Solution {
    public int N;
    public int solution(int distance, int[] rocks, int n) {
        int answer = 0;
        // 0 지점과 n 지점에는 무조건 있음.
        // rocks중에 n개 제거하였을때
        // 거리 중 최소값을 구하기
        int min = 0;
        int mid;
        int max = distance;
        
        Arrays.sort(rocks); // 바위 위치 정렬
        int[] fullRocks = Arrays.copyOf(rocks, rocks.length + 1);
        fullRocks[rocks.length] = distance;
        
        while(min <= max){
            mid = (min + max)/2; // 시험해볼 최소 거리
            int prev = 0; //시작 위치
            int removed = 0;
            
            //가능한지 확인
            for(int i=0;i<fullRocks.length; i++){
                int curr = fullRocks[i]; // 위치
                if (curr - prev < mid){ // 짧다면 제거
                    removed ++;
                }else{
                    prev = curr; // 다음 바위로 이동
                }
            }
            if(removed > n){
                // 너무 많이 제거해야하므로 안됨 -> 거리를 줄이기
                max = mid - 1;
            }else{
                answer = mid;
                min = mid + 1;
            }
        }
        return answer;
    }
}
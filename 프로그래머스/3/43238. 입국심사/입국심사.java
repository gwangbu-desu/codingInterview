class Solution {
    public long solution(int n, int[] times) {
        long answer = 0;
        long min = 1L;
        long mid;
        long max = n * 1_000_000_000L;
        while(min <= max){
            long count = 0;
            mid = (min + max) / 2;
            for(int time : times){
                // mid 타임 동안 한 심사원이 심사한 명 수 추가
                count += mid / time;
                if(count >= n) break;
            }
            if(count >= n){
                answer = mid;
                max = mid - 1;
            }else{
                min = mid + 1;
            }
        }
        
        return answer;
    }
}
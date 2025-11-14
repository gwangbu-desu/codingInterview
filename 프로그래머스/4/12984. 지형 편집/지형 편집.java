public class Solution {
    int[][] land;
    int P;
    int Q;
    public long solution(int[][] land, int P, int Q) {
        long answer = Long.MAX_VALUE;
        this.land = land;
        this.P = P;
        this.Q = Q;
        
        long right = 0;
        long left = Integer.MAX_VALUE;
        for(int[] a : land){
            for(int b: a){
                left = Math.min(left, b);
                right = Math.max(right,b);
            }
        }
        // long minimum_cost = Integer.MAX_VALUE;
        while(left<= right){
            long mid = left + (right - left) / 2 ;
            long cost = calculate(mid);
            long costRight = calculate(mid + 1);
            System.out.printf("%d %d %d %d\n",left,mid,right, cost);
            answer = Math.min(answer, cost);
            if(cost <= costRight){
                right = mid - 1;
            }else{
                left = mid + 1;
            }
            
        }
        return answer;
    }
    
    private long calculate(long level){
        long result = 0;
        for(int[] row : land){
            for(int each: row){
                long diff = level - each;
                if( diff < 0){
                    result -= diff * Q;
                }
                else if( diff > 0){
                    result += diff * P;
                }
            }
        }
        return result;
    }
}
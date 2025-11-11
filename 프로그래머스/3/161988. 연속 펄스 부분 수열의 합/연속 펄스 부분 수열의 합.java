import java.util.*;

class Solution {
    public long solution(int[] sequence) {
        long answer = 0;
        long[][] dp = new long[2][sequence.length];
        dp[0][0] += sequence[0];
        dp[1][0] -= sequence[0];
        answer = Math.max(dp[0][0],dp[1][0]);
        for(int i=1;i<sequence.length;i++){
            dp[0][i] = Math.max(dp[1][i-1],0l) + sequence[i];
            dp[1][i] = Math.max(dp[0][i-1],0l) - sequence[i];
            answer = Math.max(answer, Math.max(dp[0][i], dp[1][i]));
        }
//         Arrays.sort(dp[0]);
//         Arrays.sort(dp[1]);
        
//         for(int i:dp[0]) System.out.printf("%d ",i);
        
//         System.out.println();
//         for(int i:dp[1]) System.out.printf("%d ",i);
        
        return answer;
    }
}
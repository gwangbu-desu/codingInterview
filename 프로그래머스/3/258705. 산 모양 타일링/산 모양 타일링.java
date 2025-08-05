class Solution {
    public int solution(int n, int[] tops) {
        int MOD = 10007;
        int[] dp = new int[n + 1];
        dp[0] = 1;
        
        if (n >= 1) {
            if (tops[0] == 1) {
                dp[1] = 4; // 마름모, 아래2개, 위+아래, 위만
            } else {
                dp[1] = 3; // 마름모, 아래2개, 아래1개
            }
        }
        
        for (int i = 2; i <= n; i++) {
            if (tops[i - 1] == 1) {
                // 위쪽 삼각형이 있는 경우
                // 이전 상태에서 확장하는 방법들만 고려 (큰 삼각형 제외)
                // 계수를 다시 계산해야 함
                dp[i] = (4 * dp[i - 1] - dp[i - 2] + MOD) % MOD;
            } else {
                // 위쪽 삼각형이 없는 경우
                dp[i] = (3 * dp[i - 1] - dp[i - 2] + MOD) % MOD;
            }
        }
        
        return dp[n];
    }
}